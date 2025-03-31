from pydantic import BaseModel

class ServerMonitorCreate(BaseModel):
    server_name: str
    cpu_usage: float
    ram_usage: float
    site_status: bool
    timestamp: int

    class Config:
        orm_mode = True
