import psutil
import httpx
import paramiko
import re
from datetime import datetime


def get_cpu_usage(client):
    """Obtém o uso de CPU (%) via SSH, buscando o campo 'id' (idle) com regex"""
    try:
        stdin, stdout, stderr = client.exec_command('top -bn1 | grep "Cpu(s)"')
        output = stdout.read().decode('utf-8')

        # Expressão regular para capturar o número antes de 'id'
        match = re.search(r'(\d+[.,]?\d*)\s*id', output)
        if match:
            idle_str = match.group(1).replace(',', '.')
            idle = float(idle_str)
            usage = 100.0 - idle
            return round(usage, 2)
        else:
            return "Falha ao parsear CPU"
    except Exception as e:
        return str(e)


def get_ram_usage(client):
    """Obtém o uso de RAM em %"""
    try:
        stdin, stdout, stderr = client.exec_command('free -m')
        output = stdout.read().decode('utf-8')
        lines = output.split('\n')
        mem_line = lines[1].split()
        total = int(mem_line[1])
        used = int(mem_line[2])
        percent = (used / total) * 100
        return round(percent, 2)
    except Exception as e:
        return str(e)


def get_disk_usage(client):
    """Obtém o uso do disco (em %) da partição root /"""
    try:
        stdin, stdout, stderr = client.exec_command('df -h /')
        output = stdout.read().decode('utf-8')
        lines = output.strip().split('\n')
        if len(lines) >= 2:
            usage = lines[1].split()[4]
            return usage.strip('%')  # ex: '88'
        return "N/A"
    except Exception as e:
        return str(e)


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

def ssh_connection(ip: str, username: str, password: str):
    """Verifica a conexão SSH com a VM"""
    try:
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy()) 
        client.connect(ip, username=username, password=password)
        
        return client
    except Exception as e:
        return False
    
def close_ssh_connection(client):
    """Fecha a conexão SSH com a VM"""
    client.close()