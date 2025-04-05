from sqlalchemy import Column, Integer, String, Boolean, Float, ForeignKey
from sqlalchemy.orm import relationship
from db import Base

class VM(Base):
    __tablename__ = "vms"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)  # Nome da VM
    ip_address = Column(String, unique=True, index=True)  # IP da VM
    username = Column(String)  # Usuário de conexão
    password = Column(String)  # Senha do usuário
    root_password = Column(String, nullable=True)  # Senha de root (se houver)
    site_url = Column(String, nullable=True)  # URL do site hospedado nessa VM

    monitors = relationship("Monitoramento", back_populates="vm")  # Relacionamento com os dados coletados

class Monitoramento(Base):
    __tablename__ = "monitoramentos"

    id = Column(Integer, primary_key=True, index=True)
    vm_id = Column(Integer, ForeignKey("vms.id"))  # Referência para a VM
    cpu_usage = Column(Float)  # Uso de CPU (%)
    ram_usage = Column(Float)  # Uso de RAM (%)
    disk_free = Column(Float)  # Espaço livre em disco (GB)
    site_status = Column(Boolean)  # True se o site está no ar, False se caiu

    vm = relationship("VM", back_populates="monitors")
