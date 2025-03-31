import psutil
import httpx
from datetime import datetime

def get_cpu_usage():
    return psutil.cpu_percent(interval=1)

def get_ram_usage():
    return psutil.virtual_memory().percent

async def get_site_status(url: str):
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(url)
            return response.status_code == 200
        except:
            return False

def get_current_timestamp():
    return int(datetime.timestamp(datetime.now()))
