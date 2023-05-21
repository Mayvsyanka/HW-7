"""init migration

Revision ID: 754c94a1ead3
Revises: 
Create Date: 2023-05-20 22:57:08.436152

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '754c94a1ead3'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Groups',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('group_name', sa.String(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('Teachers',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('teacher_name', sa.String(length=100), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('Students',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('student_name', sa.String(length=50), nullable=False),
    sa.Column('group_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['group_id'], ['Groups.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('Subjects',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('subject', sa.String(length=50), nullable=False),
    sa.Column('teachers_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['teachers_id'], ['Teachers.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('Marks',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('mark', sa.Integer(), nullable=False),
    sa.Column('day', sa.Date(), nullable=False),
    sa.Column('student_id', sa.Integer(), nullable=True),
    sa.Column('subject_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['student_id'], ['Students.id'], ),
    sa.ForeignKeyConstraint(['subject_id'], ['Subjects.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('Marks')
    op.drop_table('Subjects')
    op.drop_table('Students')
    op.drop_table('Teachers')
    op.drop_table('Groups')
    # ### end Alembic commands ###