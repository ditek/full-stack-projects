"""empty message

Revision ID: 411ef175771f
Revises: b2e29ee09d9b
Create Date: 2020-05-31 00:11:47.057204

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '411ef175771f'
down_revision = 'b2e29ee09d9b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('Area')
    op.drop_column('Show', 'id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Show', sa.Column('id', sa.INTEGER(), autoincrement=False, nullable=False))
    op.create_table('Area',
    sa.Column('id', sa.INTEGER(), server_default=sa.text('nextval(\'"Area_id_seq"\'::regclass)'), autoincrement=True, nullable=False),
    sa.Column('city', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('state', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='Area_pkey')
    )
    # ### end Alembic commands ###
