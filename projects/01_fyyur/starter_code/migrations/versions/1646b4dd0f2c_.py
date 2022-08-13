"""empty message

Revision ID: 1646b4dd0f2c
Revises: 2e18d44ae781
Create Date: 2022-08-10 18:10:01.407283

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1646b4dd0f2c'
down_revision = '2e18d44ae781'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('show', sa.Column('id', sa.Integer(), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('show', 'id')
    # ### end Alembic commands ###
