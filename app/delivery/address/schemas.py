from pydantic import BaseModel

from uuid import UUID


class AddressCreate(BaseModel):
    customer_id: UUID
    first_name: str
    last_name: str
    phone_number: str
    address_line_1: str
    address_line_2: str | None = None
    city: str
    postcode: str
    country: str
    delivery_instructions: str | None = None


class AddressResponse(BaseModel):
    id: UUID
    first_name: str
    last_name: str
    phone_number: str
    address_line_1: str
    address_line_2: str | None = None
    city: str
    postcode: str
    country: str
    delivery_instructions: str | None = None
