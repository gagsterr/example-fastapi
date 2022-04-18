"""add content column to post table

Revision ID: 74254247c2f7
Revises: cc10cf92270b
Create Date: 2022-04-16 11:09:14.315676

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '74254247c2f7'
down_revision = 'cc10cf92270b'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column("posts", sa.Column("content", sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column("posts", "content")
    pass
