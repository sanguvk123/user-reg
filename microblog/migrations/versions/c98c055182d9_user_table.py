"""user table

Revision ID: c98c055182d9
Revises: d2461f6e0188
Create Date: 2020-03-03 17:49:36.286890

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c98c055182d9'
down_revision = 'd2461f6e0188'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('gender', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'gender')
    # ### end Alembic commands ###
