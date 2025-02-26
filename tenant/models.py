from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Integer, String
from core.database import Base

class Tenant(Base):
    __tablename__ = "tenants"
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(32), unique=True, nullable=False)
    description: Mapped[str] = mapped_column(String(64), unique=True, nullable=False)