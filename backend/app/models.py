from sqlalchemy import Column, Integer, String, Float, Boolean
from db import Base

class ServerMonitor(Base):
    __tablename__ = "server_monitor"

    id = Column(Integer, primary_key=True, index=True)
    server_name = Column(String, index=True)
    cpu_usage = Column(Float)
    ram_usage = Column(Float)
    site_status = Column(Boolean)
    timestamp = Column(Integer)  # Timestamp em que a coleta foi feita
