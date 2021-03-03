"""Initial migration - 2

Revision ID: b9f7493b871e
Revises: f3b55fe071b9
Create Date: 2021-02-25 21:08:52.772505

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b9f7493b871e'
down_revision = 'f3b55fe071b9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
  #  op.alter_column('content', 'paragraph_text',
  #             existing_type=sa.TEXT(),
  #             nullable=False)
  #  op.create_unique_constraint(None, 'content', ['letter_id', 'paragraph_no', 'paragraph_text'])
    # ### end Alembic commands ###
    pass

def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'content', type_='unique')
    op.alter_column('content', 'paragraph_text',
               existing_type=sa.TEXT(),
               nullable=True)
    # ### end Alembic commands ###
