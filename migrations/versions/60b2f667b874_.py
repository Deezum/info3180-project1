"""empty message

Revision ID: 60b2f667b874
Revises: 
Create Date: 2022-03-18 11:14:55.807207

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '60b2f667b874'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('property',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('proptitle', sa.String(length=100), nullable=True),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('room', sa.String(length=10), nullable=True),
    sa.Column('bathroom', sa.String(length=10), nullable=True),
    sa.Column('propprice', sa.String(length=30), nullable=True),
    sa.Column('proptype', sa.String(length=20), nullable=True),
    sa.Column('location', sa.String(length=200), nullable=True),
    sa.Column('picture', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('property')
    # ### end Alembic commands ###
