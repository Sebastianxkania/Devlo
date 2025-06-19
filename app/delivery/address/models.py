from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Integer, String
from core.database import Base

import uuid
from sqlalchemy.dialects.postgresql import UUID


class Address(Base):
    __tablename__ = "addresses"

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
    address_line_1: Mapped[str] = mapped_column(String(255), nullable=False)
    address_line_2: Mapped[str] = mapped_column(String(255), nullable=True)
    city: Mapped[str] = mapped_column(String(100), nullable=False)
    postcode: Mapped[str] = mapped_column(String(7), nullable=False)
    country: Mapped[str] = mapped_column(String(100), nullable=False)
    delivery_instructions: Mapped[str] = mapped_column(String(500), nullable=True)
