"""empty message

Revision ID: 17c6da4332a8
Revises: 5c674901eb8e
Create Date: 2024-01-21 10:04:38.510058

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '17c6da4332a8'
down_revision: Union[str, None] = '5c674901eb8e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
