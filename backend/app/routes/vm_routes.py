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
