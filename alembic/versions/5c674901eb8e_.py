"""empty message

Revision ID: 5c674901eb8e
Revises: a73cea9c1637
Create Date: 2024-01-21 10:04:31.474361

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '5c674901eb8e'
down_revision: Union[str, None] = 'a73cea9c1637'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
