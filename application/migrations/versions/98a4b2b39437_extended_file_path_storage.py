"""extended file path storage

Revision ID: 98a4b2b39437
Revises: 7a368b6a27d1
Create Date: 2019-12-09 18:07:16.342822

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '98a4b2b39437'
down_revision = '7a368b6a27d1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('post', 'body')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('post', sa.Column('body', mysql.VARCHAR(length=240), nullable=True))
    # ### end Alembic commands ###