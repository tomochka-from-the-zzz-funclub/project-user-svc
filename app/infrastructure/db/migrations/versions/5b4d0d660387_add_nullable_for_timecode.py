"""add nullable for timecode

Revision ID: 5b4d0d660387
Revises: 9485bcfaa8a6
Create Date: 2024-11-27 00:15:26.649455

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = '5b4d0d660387'
down_revision: Union[str, None] = '9485bcfaa8a6'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('viewed', 'timecode',
               existing_type=postgresql.TIME(),
               nullable=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('viewed', 'timecode',
               existing_type=postgresql.TIME(),
               nullable=False)
    # ### end Alembic commands ###