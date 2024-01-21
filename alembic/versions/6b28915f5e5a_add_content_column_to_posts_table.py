"""add content column to posts table

Revision ID: 6b28915f5e5a
Revises: 17c6da4332a8
Create Date: 2024-01-21 10:06:44.603322

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6b28915f5e5a'
down_revision: Union[str, None] = '17c6da4332a8'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
