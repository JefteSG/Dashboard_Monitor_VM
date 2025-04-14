from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db import SessionLocal
from models import VM
from schemas import VMCreate

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/vm")
async def create_vm(vm: VMCreate, db: Session = Depends(get_db)):
    """
    Cadastra uma nova VM no banco de dados.
    """
    db_vm = VM(
        name=vm.name,
        ip_address=vm.ip_address,
        username=vm.username,
        password=vm.password,
        root_password=vm.root_password,
        site_url=vm.site_url
    )
    db.add(db_vm)
    db.commit()
    db.refresh(db_vm)
    
    return db_vm

@router.get("/vms")
async def get_vms(db: Session = Depends(get_db)):
    """
    Retorna todas as VMs cadastradas no banco de dados.
    """
    vms = db.query(VM).all()
    return vms

@router.get("/vm/{vm_id}")
async def get_vm(vm_id: int, db: Session = Depends(get_db)):
    """
    Retorna uma VM específica pelo ID.
    """
    vm = db.query(VM).get(vm_id)
    if vm is None:
        raise HTTPException(status_code=404, detail="VM not found")
    return vm

@router.put("/vm/{vm_id}")
async def update_vm(vm_id: int, vm: VMCreate, db: Session = Depends(get_db)):
    """
    Atualiza uma VM existente no banco de dados.
    """
    db_vm = db.query(VM).get(vm_id)
    if db_vm is None:
        raise HTTPException(status_code=404, detail="VM not found")
    db_vm.name = vm.name
    db_vm.ip_address = vm.ip_address
    db_vm.username = vm.username
    db_vm.password = vm.password
    db_vm.root_password = vm.root_password
    db_vm.site_url = vm.site_url
    db.commit()
    return db_vm


@router.delete("/vm/{ip_address}")
async def delete_vm_by_name(ip_address: str, db: Session = Depends(get_db)):
    """
    Exclui uma VM existente no banco de dados.
    """
    db_vm = db.query(VM).filter_by(ip_address=ip_address).first()
    if db_vm is None:
        raise HTTPException(status_code=404, detail="VM not found")
    db.delete(db_vm)
    db.commit()
    return {"message": "VM deleted"}