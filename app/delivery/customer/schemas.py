from pydantic import BaseModel, Field
from typing import Optional, List
import datetime

from uuid import UUID

from app.delivery.order import schemas as OrderSchemas


class CustomerCreate(BaseModel):
    user_id: UUID


class CustomerResponse(BaseModel):
    id: UUID
    user_id: UUID
    created_at: datetime.datetime
    orders: List[OrderSchemas.OrderResponse] = []

    class Config:
        orm_mode = True
