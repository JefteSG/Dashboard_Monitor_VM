import psutil
import httpx
import paramiko
from datetime import datetime

def get_cpu_usage():
    """Obtém o uso de CPU"""
    return psutil.cpu_percent(interval=1)

def get_ram_usage():
    """Obtém o uso de RAM"""
    return psutil.virtual_memory().percent

def get_disk_usage():
    """Obtém o uso do disco"""
    disk = psutil.disk_usage('/')
    return disk.percent  # Retorna o percentual de uso do disco

async def get_site_status(url: str):
    """Verifica se o site está ativo"""
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(url)
            return response.status_code == 200
        except:
            return False

def get_current_timestamp():
    """Obtém o timestamp atual"""
    return int(datetime.timestamp(datetime.now()))

def check_ssh_connection(ip: str, username: str, password: str):
    """Verifica a conexão SSH com a VM"""
    try:
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy()) 
        client.connect(ip, username=username, password=password)
        
        stdin, stdout, stderr = client.exec_command('echo "SSH connection successful"')
        result = stdout.read().decode('utf-8')
        
        client.close()
        return "SSH connection successful" in result
    except Exception as e:
        return False

