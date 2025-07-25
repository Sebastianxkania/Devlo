"""added addresses to customer -3

Revision ID: d0a76d3e78a2
Revises: 8d8046448e33
Create Date: 2025-07-24 00:53:30.119140

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd0a76d3e78a2'
down_revision: Union[str, None] = '8d8046448e33'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('addresses', sa.Column('customer_id', sa.UUID(), nullable=False))
    op.create_foreign_key('fk_addresses_customer_id', 'addresses', 'customers', ['customer_id'], ['id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('fk_addresses_customer_id', 'addresses', type_='foreignkey')
    op.drop_column('addresses', 'customer_id')
    # ### end Alembic commands ###
