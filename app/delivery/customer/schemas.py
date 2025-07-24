from pydantic import BaseModel, Field
from typing import Optional, List
import datetime

from uuid import UUID

from app.delivery.order import schemas as OrderSchemas
from app.delivery.address import schemas as AddressSchemas


class CustomerCreate(BaseModel):
    user_id: UUID


class CustomerResponse(BaseModel):
    id: UUID
    user_id: UUID
    created_at: datetime.datetime
    orders: List[OrderSchemas.BriefOrderResponse] = []
    addresses: List[AddressSchemas.AddressResponse] = []

    class Config:
        orm_mode = True
