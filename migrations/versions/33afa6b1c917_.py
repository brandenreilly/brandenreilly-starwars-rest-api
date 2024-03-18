"""empty message

Revision ID: 33afa6b1c917
Revises: d4f331321477
Create Date: 2024-03-18 18:54:13.814296

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '33afa6b1c917'
down_revision = 'd4f331321477'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('planets',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=120), nullable=True),
    sa.Column('climate', sa.String(length=120), nullable=True),
    sa.Column('terrain', sa.String(length=120), nullable=True),
    sa.Column('population', sa.String(length=120), nullable=True),
    sa.Column('diamete', sa.String(length=120), nullable=True),
    sa.Column('gravity', sa.String(length=120), nullable=True),
    sa.Column('rotation_period', sa.String(length=120), nullable=True),
    sa.Column('orbital_period', sa.String(length=120), nullable=True),
    sa.Column('surface_water', sa.String(length=120), nullable=True),
    sa.Column('img_url', sa.String(length=120), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('planets')
    # ### end Alembic commands ###