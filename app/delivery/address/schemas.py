from pydantic import BaseModel

from uuid import UUID


class AddressCreate(BaseModel):
    address_line_1: str
    address_line_2: str | None = None
    city: str
    postcode: str
    country: str
    delivery_instructions: str | None = None


class AddressResponse(BaseModel):
    id: UUID
    address_line_1: str
    address_line_2: str | None = None
    city: str
    postcode: str
    country: str
    delivery_instructions: str | None = None
