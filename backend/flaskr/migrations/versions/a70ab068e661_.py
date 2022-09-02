"""empty message

Revision ID: a70ab068e661
Revises: 
Create Date: 2022-08-31 16:05:04.887547

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a70ab068e661'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('category', 'questions', type_='foreignkey')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_foreign_key('category', 'questions', 'categories', ['category'], ['id'], onupdate='CASCADE', ondelete='SET NULL')
    # ### end Alembic commands ###