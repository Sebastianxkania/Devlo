from fastapi import APIRouter, Depends, HTTPException

from sqlalchemy.orm import Session

from core.database import get_db

from app.delivery.order import schemas as OrderSchemas
from app.delivery.order import services as order_services


order_router = APIRouter(
    tags=["orders"],
)


@order_router.get(
    "/orders/{order_id}",
    response_model=OrderSchemas.OrderResponse,
)
def order_get(order_id: str, db: Session = Depends(get_db)):
    return order_services.get_order(db, order_id)


@order_router.post("/orders", response_model=OrderSchemas.OrderResponse)
def order_post(order: OrderSchemas.OrderCreate, db: Session = Depends(get_db)):
    return order_services.create_order(db, order)
