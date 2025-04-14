import asyncio
from fastapi import APIRouter, WebSocket, Depends
from sqlalchemy.orm import Session
from db import SessionLocal
from models import VM, Monitoramento
from schemas import MonitoramentoCreate
from services import (
    get_cpu_usage,
    get_ram_usage,
    get_disk_usage,         # Atualizado: função renomeada
    get_site_status,
    get_current_timestamp,
    ssh_connection,
    close_ssh_connection   # Para checar a conexão SSH com a VM
)

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

async def monitor_vms_ws(websocket: WebSocket, db: Session = Depends(get_db)):
    await websocket.accept()

    try:
        while True:
            vms = db.query(VM).all()

            async def process_vm(vm):
                try:
                    ssh_client = await asyncio.to_thread(ssh_connection, vm.ip_address, vm.username, vm.password)

                    if ssh_client:
                        cpu = await asyncio.to_thread(get_cpu_usage, ssh_client)
                        ram = await asyncio.to_thread(get_ram_usage, ssh_client)
                        disk = await asyncio.to_thread(get_disk_usage, ssh_client)

                        await asyncio.to_thread(close_ssh_connection, ssh_client)
                    else:
                        cpu, ram, disk = None, None, None

                    site_status = await get_site_status(vm.site_url) if vm.site_url else False

                    return {
                        "vm_name": vm.name,
                        "cpu_usage": cpu,
                        "ram_usage": ram,
                        "disk_usage": disk,
                        "site_status": site_status,
                        "ssh_status": True if ssh_client else False,
                        "ip": vm.ip_address,
                        "user": vm.username,
                        "password": vm.password,
                        "site": vm.site_url
                    }

                except Exception as e:
                    return {
                        "vm_name": vm.name,
                        "error": str(e)
                    }

            # Executa todas as VMs em paralelo
            tasks = [process_vm(vm) for vm in vms]
            response_data = await asyncio.gather(*tasks)

            # Envia os dados pro frontend
            await websocket.send_json(response_data)

            await asyncio.sleep(5)

    except Exception as e:
        print(f"Erro na conexão WebSocket: {e}")
    finally:
        await websocket.close()
