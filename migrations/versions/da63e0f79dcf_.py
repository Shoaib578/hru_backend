"""empty message

Revision ID: da63e0f79dcf
Revises: 16e29b1cba0d
Create Date: 2023-06-25 14:33:51.989741

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'da63e0f79dcf'
down_revision = '16e29b1cba0d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('lectures', schema=None) as batch_op:
        batch_op.alter_column('lecture_number',
               existing_type=mysql.INTEGER(display_width=11),
               nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('lectures', schema=None) as batch_op:
        batch_op.alter_column('lecture_number',
               existing_type=mysql.INTEGER(display_width=11),
               nullable=False)

    # ### end Alembic commands ###
