"""empty message

Revision ID: 991f632f122c
Revises: 
Create Date: 2023-07-27 15:09:49.870897

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '991f632f122c'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('applications',
    sa.Column('application_id', sa.Integer(), nullable=False),
    sa.Column('resume', sa.String(length=200), nullable=True),
    sa.Column('email', sa.String(length=200), nullable=True),
    sa.PrimaryKeyConstraint('application_id')
    )
    op.create_table('panel_users',
    sa.Column('panel_userid', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=150), nullable=False),
    sa.Column('name', sa.String(length=200), nullable=False),
    sa.Column('phone', sa.String(length=100), nullable=True),
    sa.Column('password', sa.String(length=255), nullable=False),
    sa.Column('profile_picture', sa.String(length=300), nullable=True),
    sa.Column('title', sa.String(length=300), nullable=True),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('is_admin', sa.Integer(), nullable=False),
    sa.Column('is_teacher', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('panel_userid')
    )
    with op.batch_alter_table('panel_users', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_panel_users_email'), ['email'], unique=False)

    op.create_table('pending_withdrawals',
    sa.Column('p_withdrawal_id', sa.Integer(), nullable=False),
    sa.Column('bank_iban_number', sa.String(length=255), nullable=True),
    sa.Column('email', sa.String(length=255), nullable=True),
    sa.Column('full_name', sa.String(length=255), nullable=True),
    sa.Column('is_paid', sa.Boolean(), nullable=True),
    sa.Column('total_amount', sa.Integer(), nullable=True),
    sa.Column('paid_date', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('p_withdrawal_id')
    )
    op.create_table('users',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=40), nullable=False),
    sa.Column('email', sa.String(length=255), nullable=False),
    sa.Column('password', sa.String(length=255), nullable=False),
    sa.Column('phone_no', sa.String(length=255), nullable=True),
    sa.Column('address', sa.String(length=255), nullable=True),
    sa.Column('stripe_id', sa.String(length=255), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('user_id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('courses',
    sa.Column('course_id', sa.Integer(), nullable=False),
    sa.Column('course_title', sa.String(length=300), nullable=True),
    sa.Column('course_description', sa.String(length=2000), nullable=True),
    sa.Column('teacher_id', sa.Integer(), nullable=True),
    sa.Column('course_thumbnail', sa.String(length=200), nullable=True),
    sa.Column('course_price', sa.Integer(), nullable=True),
    sa.Column('course_category', sa.String(length=100), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['teacher_id'], ['panel_users.panel_userid'], ),
    sa.PrimaryKeyConstraint('course_id')
    )
    op.create_table('wallets',
    sa.Column('wallet_id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('amount', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.user_id'], ),
    sa.PrimaryKeyConstraint('wallet_id')
    )
    op.create_table('coupons',
    sa.Column('coupon_id', sa.Integer(), nullable=False),
    sa.Column('coupon_code', sa.String(length=100), nullable=True),
    sa.Column('course_id', sa.Integer(), nullable=True),
    sa.Column('discount_percentage', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['course_id'], ['courses.course_id'], ),
    sa.PrimaryKeyConstraint('coupon_id')
    )
    op.create_table('featured_courses',
    sa.Column('featured_id', sa.Integer(), nullable=False),
    sa.Column('course_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['course_id'], ['courses.course_id'], ),
    sa.PrimaryKeyConstraint('featured_id')
    )
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
    op.create_table('links',
    sa.Column('shared_link_id', sa.Integer(), nullable=False),
    sa.Column('link', sa.String(length=300), nullable=True),
    sa.Column('shared_by', sa.Integer(), nullable=True),
    sa.Column('code', sa.String(length=100), nullable=True),
    sa.Column('course_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['course_id'], ['courses.course_id'], ),
    sa.ForeignKeyConstraint(['shared_by'], ['users.user_id'], ),
    sa.PrimaryKeyConstraint('shared_link_id')
    )
    op.create_table('owned_courses',
    sa.Column('owned_id', sa.Integer(), nullable=False),
    sa.Column('owned_by', sa.Integer(), nullable=True),
    sa.Column('course_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['course_id'], ['courses.course_id'], ),
    sa.ForeignKeyConstraint(['owned_by'], ['users.user_id'], ),
    sa.PrimaryKeyConstraint('owned_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('owned_courses')
    op.drop_table('links')
    op.drop_table('lectures')
    op.drop_table('featured_courses')
    op.drop_table('coupons')
    op.drop_table('wallets')
    op.drop_table('courses')
    op.drop_table('users')
    op.drop_table('pending_withdrawals')
    with op.batch_alter_table('panel_users', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_panel_users_email'))

    op.drop_table('panel_users')
    op.drop_table('applications')
    # ### end Alembic commands ###