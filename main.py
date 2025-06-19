from fastapi import FastAPI
from core.config import Settings
from starlette.middleware.cors import CORSMiddleware

from core.database import Base, engine

from app.delivery.customer.router import customer_router
from app.delivery.address.router import address_router
from app.delivery.order.router import order_router

Base.metadata.create_all(bind=engine)

settings = Settings()
app = FastAPI()

if settings.BACKEND_CORS_ORIGINS:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin).strip("/") for origin in settings.BACKEND_CORS_ORIGINS],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

app.include_router(customer_router, prefix="/api")
app.include_router(address_router, prefix="/api")
app.include_router(order_router, prefix="/api")


@app.get("/")
def read_root():
    return {"Hello": "World"}
