from sqlalchemy.orm import Session

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

    new_customer = CustomerModels.Customer(**customer.model_dump())

    db.add(new_customer)
    db.commit()
    db.refresh(new_customer)
    return new_customer


def get_customer(db: Session, customer_id: str) -> CustomerSchemas.CustomerResponse | None:
    """
    Get a customer by ID.
    Args:
        db: Session.
        customer_id: UUID of the customer.
    Returns:
        CustomerSchemas.CustomerResponse | None: The customer if found, otherwise None.
    """

    return db.query(CustomerModels.Customer).filter(CustomerModels.Customer.id == customer_id).first()
