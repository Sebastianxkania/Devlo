from __future__ import annotations
from sqlalchemy import Integer, String, DateTime, Boolean, ForeignKey, Enum as SAEnum, Numeric, Text
from sqlalchemy.orm import Mapped, mapped_column, declarative_base, relationship
import enum
import datetime
from core.database import Base

import uuid
from sqlalchemy.dialects.postgresql import UUID

from app.delivery.customer.models import Customer


class Order(Base):
    __tablename__ = "orders"

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)

    customer_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), ForeignKey("customers.id", name="fk_orders_customer_id"), nullable=False)
    # courier_id: Mapped[int | None] = mapped_column(Integer, ForeignKey("couriers.id"), nullable=True)

    pickup_address_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), ForeignKey("addresses.id", name="fk_orders_pickup_address_id"), nullable=False)
    delivery_address_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), ForeignKey("addresses.id", name="fk_orders_delivery_address_id"), nullable=False)

    # status: Mapped[status_models.OrderStatus] = mapped_column(SAEnum(status_models.OrderStatus), default=status_models.OrderStatus.PENDING, nullable=False)
    scheduled_time: Mapped[datetime.datetime | None] = mapped_column(DateTime(timezone=True))
    picked_up_at: Mapped[datetime.datetime | None] = mapped_column(DateTime(timezone=True))
    delivered_at: Mapped[datetime.datetime | None] = mapped_column(DateTime(timezone=True))
    created_at: Mapped[datetime.datetime] = mapped_column(DateTime(timezone=True), default=lambda: datetime.datetime.now(datetime.timezone.utc))
    updated_at: Mapped[datetime.datetime] = mapped_column(
        DateTime(timezone=True), default=lambda: datetime.datetime.now(datetime.timezone.utc), onupdate=lambda: datetime.datetime.now(datetime.timezone.utc)
    )

    # Relationships
    customer: Mapped["Customer"] = relationship("Customer", back_populates="orders")
