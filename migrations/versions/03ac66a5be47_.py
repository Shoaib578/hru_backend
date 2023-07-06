"""empty message

Revision ID: 03ac66a5be47
Revises: da63e0f79dcf
Create Date: 2023-06-25 14:38:20.632450

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '03ac66a5be47'
down_revision = 'da63e0f79dcf'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('lectures',
    sa.Column('lecture_id', sa.Integer(), nullable=False),
    sa.Column('lecture_number', sa.Integer(), nullable=True),
    sa.Column('lecture_title', sa.String(length=300), nullable=True),
    sa.Column('course_id', sa.Integer(), nullable=True),
    sa.Column('lecture_description', sa.String(length=2000), nullable=True),
    sa.Column('lecture_video', sa.String(length=200), nullable=True),
    sa.Column('lecture_type', sa.String(length=100), nullable=True),
    sa.Column('lecture_duration', sa.Integer(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['course_id'], ['courses.course_id'], ),
    sa.PrimaryKeyConstraint('lecture_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('lectures')
    # ### end Alembic commands ###