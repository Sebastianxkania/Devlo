from sqlalchemy.orm import Session

from tenant.models import Tenant
from tenant.schemas import TenantCreate


def create_tenant(db: Session, tenant: TenantCreate):
    db_tenant = Tenant(
        name=tenant.name,
        description=tenant.description,
    )
    db.add(db_tenant)
    db.commit()
    db.refresh(db_tenant)
    return db_tenant


def get_tenants(db: Session):
    return db.query(Tenant).all()

def get_tenant(db: Session, tenant_id: int):
    return db.query(Tenant).filter(Tenant.id == tenant_id).first()

def delete_tenant(db: Session, tenant_id: int):
  db_tenant = db.query(Tenant).filter(Tenant.id == tenant_id).first()
  db.delete(db_tenant)
  db.commit()
  # db.refresh(db_tenant)
  return

