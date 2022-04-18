"""add last few columns to posts table

Revision ID: de8b5f544a1a
Revises: f68f3d006910
Create Date: 2022-04-16 14:38:25.138404

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'de8b5f544a1a'
down_revision = 'f68f3d006910'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column("posts", sa.Column(
        "published", sa.Boolean(), nullable=False, server_default="True"),)
    op.add_column("posts", sa.Column(
        "created_at", sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text("NOW()")),)
    pass


def downgrade():
    op.drop_column("posts", "published")
    op.drop_column("posts", "created_at")
    pass
