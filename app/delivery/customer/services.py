from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from app.delivery.customer import schemas as CustomerSchemas
from app.delivery.customer import models as CustomerModels
from uuid import UUID


def create_customer(db: Session, customer: CustomerSchemas.CustomerCreate) -> CustomerSchemas.CustomerResponse:
    """
    Create a new customer.
    Args:
        customer: CustomerSchemas.CustomerCreate.
        db: Session.
    Returns:
        CustomerSchemas.CustomerResponse: The created customer.
    """

    try:
        new_customer = CustomerModels.Customer(**customer.model_dump())

        db.add(new_customer)
        db.commit()
        db.refresh(new_customer)

    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=(f"Error when creating new customer: {str(e)}"))

    return new_customer


def get_customer(db: Session, customer_id: str) -> CustomerSchemas.CustomerResponse:
    """
    Get a customer by ID.
    Args:
        db: Session.
        customer_id: UUID of the customer.
    Returns:
        CustomerSchemas.CustomerResponse | None: The customer if found, otherwise None.
    """

    customer = db.query(CustomerModels.Customer).filter(CustomerModels.Customer.id == customer_id).first()

    if not customer:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Customer not found")

    return customer
