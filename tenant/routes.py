from fastapi import APIRouter, Depends, HTTPException

from sqlalchemy.orm import Session

from core.database import get_db
from tenant.schemas import TenantSchema, TenantCreate
from tenant.services import create_tenant, get_tenants, get_tenant, delete_tenant

tenant_router = APIRouter()

@tenant_router.post("/tenants", response_model=TenantSchema)
def tenant_post(user: TenantCreate, db:Session = Depends(get_db)):
    return create_tenant(db, user)


@tenant_router.get('/tenants', response_model=list[TenantSchema])
def tenants_get(db: Session = Depends(get_db)):
    db_tenants = get_tenants(db)

    return db_tenants

@tenant_router.get('/tenants/{tenant_id}', response_model=TenantSchema)
def tenant_get(tenant_id: int, db: Session = Depends(get_db)):
    db_tenants = get_tenant(db, tenant_id)
    if db_tenants is None:
        raise HTTPException(status_code=404, detail="Tenant not found")

    return db_tenants


@tenant_router.delete('/tenants/{tenant_id}')
def tenant_delete(tenant_id: int, db: Session = Depends(get_db)):
    db_tenants = get_tenant(db, tenant_id)
    if db_tenants is None:
        raise HTTPException(status_code=404, detail="User not found")

    delete_tenant(db, tenant_id)
    return {"message": "User deleted"}
  


