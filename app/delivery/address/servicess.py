from sqlalchemy.orm import Session


from app.delivery.address import schemas as AddressSchemas
from app.delivery.address import models as AddressModels


def create_address(db: Session, address: AddressSchemas.AddressCreate) -> AddressSchemas.AddressResponse:
    """
    Create a new address.

    Args:
        address: AddressModels.AddressCreate.
        db: Session.

    Returns:
        AddressModels.AddressResponse: The created address.
    """

    new_address = AddressModels.Address(**address.model_dump())

    db.add(new_address)
    db.commit()
    db.refresh(new_address)
    return new_address
