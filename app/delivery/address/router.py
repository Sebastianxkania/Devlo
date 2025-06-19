from fastapi import APIRouter, Depends, HTTPException

from sqlalchemy.orm import Session

from core.database import get_db
from app.delivery.address import schemas as AddressSchemas
from app.delivery.address import servicess as address_services

address_router = APIRouter(
    tags=["addresses"],
)


@address_router.post("/addresses", response_model=AddressSchemas.AddressResponse)
def address_post(address: AddressSchemas.AddressCreate, db: Session = Depends(get_db)):
    return address_services.create_address(db, address)
