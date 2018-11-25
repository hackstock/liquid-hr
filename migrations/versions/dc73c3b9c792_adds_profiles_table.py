"""adds profiles table

Revision ID: dc73c3b9c792
Revises: 63dd85e6298c
Create Date: 2018-11-25 20:59:03.681171

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'dc73c3b9c792'
down_revision = '63dd85e6298c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('profiles',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.Column('gender', sa.String(length=255), nullable=False),
    sa.Column('phone_number', sa.String(length=255), nullable=False),
    sa.Column('private_email', sa.String(length=255), nullable=False),
    sa.Column('house_address', sa.String(length=255), nullable=True),
    sa.Column('postal_code', sa.String(length=255), nullable=True),
    sa.Column('town', sa.String(length=255), nullable=True),
    sa.Column('nationality', sa.String(length=255), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('profiles')
    # ### end Alembic commands ###