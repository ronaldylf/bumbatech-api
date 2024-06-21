"""create users table

Revision ID: dacd4975b274
Revises: 
Create Date: 2024-06-18 21:03:38.672607

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'dacd4975b274'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('users_tb',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('email', sa.String(length=320), nullable=True),
    sa.Column('senha', sa.String(length=320), nullable=True),
    sa.Column('nome', sa.String(length=100), nullable=True),
    sa.Column('idade', sa.Integer(), nullable=True),
    sa.Column('genero', sa.Integer(), nullable=True),
    sa.Column('estado', sa.String(length=30), nullable=True),
    sa.Column('cidade', sa.String(length=100), nullable=True),
    sa.Column('trilha', sa.Integer(), nullable=True),
    sa.Column('conhece_a_cultura', sa.Integer(), nullable=True),
    sa.Column('mais_se_interessa', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )


def downgrade() -> None:
    op.drop_table('users_tb')
