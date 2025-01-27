"""empty message

Revision ID: 728ea8ef4dd8
Revises: 530c2c5dbf64
Create Date: 2020-10-20 18:10:57.626379

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '728ea8ef4dd8'
down_revision = '530c2c5dbf64'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('artists',
    sa.Column('artist_id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('city', sa.String(length=120), nullable=True),
    sa.Column('state', sa.String(length=120), nullable=True),
    sa.Column('phone', sa.String(length=120), nullable=True),
    sa.Column('genres', sa.ARRAY(sa.String()), nullable=True),
    sa.Column('image_link', sa.String(length=500), nullable=True),
    sa.Column('facebook_link', sa.String(length=120), nullable=True),
    sa.Column('seeking_venue', sa.Boolean(), nullable=True),
    sa.Column('seeking_description', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('artist_id')
    )
    op.create_table('venues',
    sa.Column('venue_id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('city', sa.String(length=120), nullable=True),
    sa.Column('state', sa.String(length=120), nullable=True),
    sa.Column('address', sa.String(length=120), nullable=True),
    sa.Column('phone', sa.String(length=120), nullable=True),
    sa.Column('genres', postgresql.ARRAY(sa.String()), nullable=True),
    sa.Column('website', sa.String(length=500), nullable=True),
    sa.Column('image_link', sa.String(length=500), nullable=True),
    sa.Column('facebook_link', sa.String(length=120), nullable=True),
    sa.Column('seeking_talent', sa.Boolean(), nullable=True),
    sa.Column('seeking_description', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('venue_id')
    )
    op.create_table('shows',
    sa.Column('show_id', sa.Integer(), nullable=False),
    sa.Column('artist_id', sa.Integer(), nullable=True),
    sa.Column('venue_id', sa.Integer(), nullable=True),
    sa.Column('start_time', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['artist_id'], ['artists.artist_id'], ),
    sa.ForeignKeyConstraint(['venue_id'], ['venues.venue_id'], ),
    sa.PrimaryKeyConstraint('show_id')
    )
    op.drop_table('show')
    op.drop_table('artist')
    op.drop_table('venue')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('venue',
    sa.Column('id', sa.INTEGER(), server_default=sa.text("nextval('venue_id_seq'::regclass)"), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('genres', postgresql.ARRAY(sa.VARCHAR()), autoincrement=False, nullable=True),
    sa.Column('address', sa.VARCHAR(length=120), autoincrement=False, nullable=True),
    sa.Column('city', sa.VARCHAR(length=120), autoincrement=False, nullable=True),
    sa.Column('state', sa.VARCHAR(length=120), autoincrement=False, nullable=True),
    sa.Column('phone', sa.VARCHAR(length=120), autoincrement=False, nullable=True),
    sa.Column('image_link', sa.VARCHAR(length=500), autoincrement=False, nullable=True),
    sa.Column('facebook_link', sa.VARCHAR(length=120), autoincrement=False, nullable=True),
    sa.Column('website', sa.VARCHAR(length=120), autoincrement=False, nullable=True),
    sa.Column('seeking_talent', sa.BOOLEAN(), autoincrement=False, nullable=True),
    sa.Column('seeking_description', sa.VARCHAR(length=500), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='venue_pkey'),
    postgresql_ignore_search_path=False
    )
    op.create_table('artist',
    sa.Column('id', sa.INTEGER(), server_default=sa.text("nextval('artist_id_seq'::regclass)"), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('genres', postgresql.ARRAY(sa.VARCHAR()), autoincrement=False, nullable=True),
    sa.Column('city', sa.VARCHAR(length=120), autoincrement=False, nullable=True),
    sa.Column('state', sa.VARCHAR(length=120), autoincrement=False, nullable=True),
    sa.Column('phone', sa.VARCHAR(length=120), autoincrement=False, nullable=True),
    sa.Column('website', sa.VARCHAR(length=120), autoincrement=False, nullable=True),
    sa.Column('image_link', sa.VARCHAR(length=500), autoincrement=False, nullable=True),
    sa.Column('facebook_link', sa.VARCHAR(length=120), autoincrement=False, nullable=True),
    sa.Column('seeking_venue', sa.BOOLEAN(), autoincrement=False, nullable=True),
    sa.Column('seeking_description', sa.VARCHAR(length=500), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='artist_pkey'),
    postgresql_ignore_search_path=False
    )
    op.create_table('show',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('artist_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('venue_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('start_time', postgresql.TIMESTAMP(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['artist_id'], ['artist.id'], name='show_artist_id_fkey'),
    sa.ForeignKeyConstraint(['venue_id'], ['venue.id'], name='show_venue_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='show_pkey')
    )
    op.drop_table('shows')
    op.drop_table('venues')
    op.drop_table('artists')
    # ### end Alembic commands ###
