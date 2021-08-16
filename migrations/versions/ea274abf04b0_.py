"""empty message

Revision ID: ea274abf04b0
Revises: f56d81a76a1e
Create Date: 2021-04-11 01:21:25.479935

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ea274abf04b0'
down_revision = 'f56d81a76a1e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('account', sa.Column('public_id', sa.String(length=50), nullable=True))
    op.create_unique_constraint(None, 'account', ['public_id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'account', type_='unique')
    op.drop_column('account', 'public_id')
    # ### end Alembic commands ###
