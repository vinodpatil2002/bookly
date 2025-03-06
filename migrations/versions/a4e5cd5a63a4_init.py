"""init

Revision ID: a4e5cd5a63a4
Revises: 7e157e177e03
Create Date: 2025-03-06 22:07:16.377215

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlmodel


# revision identifiers, used by Alembic.
revision: str = 'a4e5cd5a63a4'
down_revision: Union[str, None] = '7e157e177e03'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
