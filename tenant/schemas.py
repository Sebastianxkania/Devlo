from pydantic import BaseModel

class TenantBase(BaseModel):
    name: str
    description: str

class TenantCreate(TenantBase):
    """
    Schema used when creating a new tenant.
    """
    pass

class TenantSchema(TenantBase):
    id: int

    class Config:
        orm_mode = True
