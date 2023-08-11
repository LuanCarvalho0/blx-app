"""Nova coluna Tamanho

Revision ID: 723f6d5c8240
Revises: 1f7d441a9149
Create Date: 2023-08-11 16:14:49.599045

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '723f6d5c8240'
down_revision: Union[str, None] = '1f7d441a9149'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('produto', sa.Column('tamanho', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('produto', 'tamanho')
    # ### end Alembic commands ###
