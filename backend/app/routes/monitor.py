from fastapi import APIRouter, Depends
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
    check_ssh_connection   # Para checar a conexão SSH com a VM
)

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/monitor")
async def monitor_vms(db: Session = Depends(get_db)):
    """
    Atualiza e retorna o status de todas as VMs cadastradas no banco de dados.
    """
    vms = db.query(VM).all()
    response_data = []

    for vm in vms:
        try:
            # Checa a conexão SSH da VM
            ssh_status = check_ssh_connection(vm.ip_address, vm.username, vm.password)
            
            # Se a conexão SSH for bem-sucedida, coleta os dados;
            # caso contrário, deixa os valores como None (ou zero)
            if ssh_status:
                cpu = get_cpu_usage()       # Se necessário, adaptar para coleta remota
                ram = get_ram_usage()
                disk = get_disk_usage()     # Aqui usamos a função atualizada
            else:
                cpu, ram, disk = None, None, None

            # Checa o status do site, se a URL estiver definida
            site_status = await get_site_status(vm.site_url) if vm.site_url else False

            # Cria o objeto de monitoramento para inserir no banco
            monitor_data = MonitoramentoCreate(
                vm_id=vm.id,
                cpu_usage=cpu if cpu is not None else 0,
                ram_usage=ram if ram is not None else 0,
                disk_free=disk if disk is not None else 0,
                site_status=site_status
            )
            
            monitor_instance = Monitoramento(**monitor_data.dict())
            db.add(monitor_instance)
            db.commit()
            
            response_data.append({
                "vm_name": vm.name,
                "cpu_usage": cpu,
                "ram_usage": ram,
                "disk_usage": disk,
                "site_status": site_status,
                "ssh_status": ssh_status
            })
        except Exception as e:
            response_data.append({
                "vm_name": vm.name,
                "error": str(e)
            })

    return response_data
