from pydantic import BaseModel

class ServerMonitorCreate(BaseModel):
    server_name: str
    cpu_usage: float
    ram_usage: float
    site_status: bool
    timestamp: int

    class Config:
        orm_mode = True

from pydantic import BaseModel, Field
from typing import Optional

class VMCreate(BaseModel):
    name: str
    ip_address: str
    username: str
    password: str
    root_password: Optional[str] = None
    site_url: Optional[str] = None

class MonitoramentoCreate(BaseModel):
    vm_id: int
    cpu_usage: float
    ram_usage: float
    disk_free: float
    site_status: bool
