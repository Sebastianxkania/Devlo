from sqlalchemy.orm import Session

from app.delivery.order import schemas as OrderSchemas
from app.delivery.order import models as OrderModels


def create_order(db: Session, order: OrderSchemas.OrderCreate) -> OrderSchemas.OrderResponse:
    """
    Create a new order in the database.
    Args:
        db (Session): The database session.
        order (OrderSchemas.OrderCreate): The order data to create.
    Returns:
        OrderSchemas.OrderResponse: The created order.
    """

    new_order = OrderModels.Order(**order.model_dump())

    db.add(new_order)
    db.commit()
    db.refresh(new_order)
    return new_order
