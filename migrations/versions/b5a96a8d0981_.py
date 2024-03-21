"""empty message

Revision ID: b5a96a8d0981
Revises: 1212aa4a9d58
Create Date: 2024-03-21 15:19:17.022427

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b5a96a8d0981'
down_revision = '1212aa4a9d58'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('favorites', schema=None) as batch_op:
        batch_op.add_column(sa.Column('char_id', sa.String(length=120), nullable=True))
        batch_op.add_column(sa.Column('planet_id', sa.String(length=120), nullable=True))
        batch_op.drop_column('uid')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('favorites', schema=None) as batch_op:
        batch_op.add_column(sa.Column('uid', sa.VARCHAR(length=120), autoincrement=False, nullable=True))
        batch_op.drop_column('planet_id')
        batch_op.drop_column('char_id')

    # ### end Alembic commands ###