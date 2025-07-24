from pydantic import BaseModel
from uuid import UUID
from datetime import datetime


class OrderCreate(BaseModel):
    customer_id: UUID
    pickup_address_id: UUID
    delivery_address_id: UUID
    # scheduled_time: datetime | None = None
    # picked_up_at: datetime | None = None
    # delivered_at: datetime | None = None


class BriefOrderResponse(BaseModel):
    id: UUID

    class Config:
        orm_mode = True


class OrderResponse(BaseModel):
    id: UUID
    customer_id: UUID
    pickup_address_id: UUID
    delivery_address_id: UUID
    scheduled_time: datetime | None = None
    picked_up_at: datetime | None = None
    delivered_at: datetime | None = None
    created_at: datetime
    updated_at: datetime
