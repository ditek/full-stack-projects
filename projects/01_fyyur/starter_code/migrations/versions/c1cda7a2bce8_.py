"""empty message

Revision ID: c1cda7a2bce8
Revises: 119790bb9987
Create Date: 2020-05-31 02:23:33.924913

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c1cda7a2bce8'
down_revision = '119790bb9987'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('Venue_area_id_fkey', 'Venue', type_='foreignkey')
    op.drop_column('Venue', 'area_id')
    op.drop_table('Area')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Venue', sa.Column('area_id', sa.INTEGER(), autoincrement=False, nullable=False))
    op.create_foreign_key('Venue_area_id_fkey', 'Venue', 'Area', ['area_id'], ['id'])
    op.create_table('Area',
    sa.Column('id', sa.INTEGER(), server_default=sa.text('nextval(\'"Area_id_seq"\'::regclass)'), autoincrement=True, nullable=False),
    sa.Column('city', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('state', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='Area_pkey')
    )
    # ### end Alembic commands ###
