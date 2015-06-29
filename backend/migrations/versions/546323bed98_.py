"""empty message

Revision ID: 546323bed98
Revises: None
Create Date: 2015-06-29 11:11:38.614537

"""

# revision identifiers, used by Alembic.
revision = '546323bed98'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('boards',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('shortname', sa.String(length=10), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('description', sa.Unicode(length=200), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('boards')
    ### end Alembic commands ###
