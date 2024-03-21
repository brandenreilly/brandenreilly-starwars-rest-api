"""empty message

Revision ID: bb99a95eae1e
Revises: b5a96a8d0981
Create Date: 2024-03-21 15:32:21.376841

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bb99a95eae1e'
down_revision = 'b5a96a8d0981'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('favorites', schema=None) as batch_op:
        batch_op.add_column(sa.Column('typeof', sa.String(length=120), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('favorites', schema=None) as batch_op:
        batch_op.drop_column('typeof')

    # ### end Alembic commands ###