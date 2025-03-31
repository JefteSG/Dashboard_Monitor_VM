from fastapi import APIRouter
from services import get_cpu_usage, get_ram_usage, get_site_status, get_current_timestamp
from db import SessionLocal
from models import ServerMonitor
from schemas import ServerMonitorCreate

router = APIRouter()

@router.get("/monitor")
async def monitor():
    cpu = get_cpu_usage()
    ram = get_ram_usage()
    site_status = await get_site_status("https://jef-prod.nx1.app.br/")  # Substitua com o site desejado
    
    data = ServerMonitorCreate(
        server_name="Servidor1",  # Nome do servidor
        cpu_usage=cpu,
        ram_usage=ram,
        site_status=site_status,
        timestamp=get_current_timestamp()
    )

    db = SessionLocal()
    db.add(ServerMonitor(**data.dict()))
    db.commit()
    db.close()

    return {"cpu_usage": cpu, "ram_usage": ram, "site_status": site_status}
