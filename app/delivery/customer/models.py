from sqlalchemy import Integer, String, DateTime, Boolean, ForeignKey, Enum as SAEnum, Numeric, Text
from sqlalchemy.orm import Mapped, mapped_column, declarative_base, relationship
import enum
import datetime
from core.database import Base
import uuid
from sqlalchemy.dialects.postgresql import UUID


class Customer(Base):
    __tablename__ = "customers"
    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
    # user_id: Mapped[str] = mapped_column(String(36), nullable=True)
    user_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), default=uuid.uuid4, unique=True, nullable=False)
    created_at: Mapped[datetime.datetime] = mapped_column(DateTime(timezone=True), default=lambda: datetime.datetime.now(datetime.timezone.utc))

    orders = relationship(
        "Order",
        back_populates="customer",
        cascade="all, delete-orphan",
    )

    addresses = relationship(
        "Address",
        back_populates="customer",
        cascade="all, delete-orphan",
    )
