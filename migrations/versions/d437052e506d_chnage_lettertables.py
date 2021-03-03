"""Chnage LetterTables

Revision ID: d437052e506d
Revises: 53c88f88392c
Create Date: 2021-03-03 03:31:41.109744

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd437052e506d'
down_revision = '53c88f88392c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('lettertable',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('letter_id', sa.Integer(), nullable=False),
    sa.Column('table_no', sa.Integer(), nullable=False),
    sa.Column('row', sa.Integer(), nullable=False),
    sa.Column('col', sa.Integer(), nullable=False),
    sa.Column('detail', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('letter_id', 'table_no', 'row', 'col')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('lettertable')
    # ### end Alembic commands ###
