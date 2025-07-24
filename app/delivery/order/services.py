from sqlalchemy.orm import Session
from fastapi import HTTPException, status

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

    try:

        new_order = OrderModels.Order(**order.model_dump())

        db.add(new_order)
        db.commit()
        db.refresh(new_order)

    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=400, detail=f"Error when creating new order: {str(e)}")

    return new_order


def get_order(db: Session, order_id: str) -> OrderSchemas.OrderResponse:
    """
    Get an order by its ID.
    Args:
        db (Session): The database session.
        order_id (str): The ID of the order to retrieve.
    Returns:
        OrderSchemas.OrderResponse | None: The order if found, otherwise None.
    """

    order = db.query(OrderModels.Order).filter(OrderModels.Order.id == order_id).first()

    if not order:
        raise HTTPException(status_code=404, detail="Order not found")

    return order
