"""add user table

Revision ID: bec6854aa721
Revises: 74254247c2f7
Create Date: 2022-04-16 11:14:33.634841

"""
from alembic import op
from fastapi import FastAPI
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bec6854aa721'
down_revision = '74254247c2f7'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table("users",
                    sa.Column("id", sa.Integer(), nullable=False),
                    sa.Column("email", sa.String(), nullable=False),
                    sa.Column("password", sa.String(), nullable=False),
                    sa.Column("created_at", sa.TIMESTAMP(timezone=True),
                                server_default=sa.text("now()"), nullable=False),
                    sa.PrimaryKeyConstraint("id"),
                    sa.UniqueConstraint("email")
                    )
    pass


def downgrade():
    op.drop_table("users")
    pass
