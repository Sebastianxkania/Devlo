from fastapi import APIRouter, Depends, HTTPException

from sqlalchemy.orm import Session

from core.database import get_db

from uuid import UUID

from app.delivery.customer import schemas as CustomerSchemas
from app.delivery.customer import services as customer_services

customer_router = APIRouter(
    tags=["customers"],
)


@customer_router.get(
    "/customers/{customer_id}",
    response_model=CustomerSchemas.CustomerResponse,
)
def customer_get(customer_id: str, db: Session = Depends(get_db)):
    return customer_services.get_customer(db, customer_id)


@customer_router.post("/customers", response_model=CustomerSchemas.CustomerResponse)
def customer_post(customer: CustomerSchemas.CustomerCreate, db: Session = Depends(get_db)):
    return customer_services.create_customer(db, customer)
