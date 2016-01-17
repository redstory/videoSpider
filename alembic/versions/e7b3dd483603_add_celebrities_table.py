"""Add celebrities table

Revision ID: e7b3dd483603
Revises: 54b5db82884c
Create Date: 2016-01-18 00:20:06.629556

"""

# revision identifiers, used by Alembic.
revision = 'e7b3dd483603'
down_revision = '54b5db82884c'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('celebrities',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('douban_id', sa.String(), nullable=True),
    sa.Column('douban_url', sa.String(), nullable=True),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('name_en', sa.String(), nullable=True),
    sa.Column('cover', sa.String(), nullable=True),
    sa.Column('website', sa.String(), nullable=True),
    sa.Column('gender', sa.String(), nullable=True),
    sa.Column('birthday', sa.String(), nullable=True),
    sa.Column('born_place', sa.String(), nullable=True),
    sa.Column('professions', sa.String(), nullable=True),
    sa.Column('constellation', sa.String(), nullable=True),
    sa.Column('photos', sa.String(), nullable=True),
    sa.Column('imdb_number', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('subjects_actors',
    sa.Column('subject_id', sa.Integer(), nullable=True),
    sa.Column('celebrity_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['celebrity_id'], ['celebrities.id'], ),
    sa.ForeignKeyConstraint(['subject_id'], ['subjects.id'], )
    )
    op.create_table('subjects_directors',
    sa.Column('subject_id', sa.Integer(), nullable=True),
    sa.Column('celebrity_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['celebrity_id'], ['celebrities.id'], ),
    sa.ForeignKeyConstraint(['subject_id'], ['subjects.id'], )
    )
    op.create_table('subjects_playwrights',
    sa.Column('subject_id', sa.Integer(), nullable=True),
    sa.Column('celebrity_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['celebrity_id'], ['celebrities.id'], ),
    sa.ForeignKeyConstraint(['subject_id'], ['subjects.id'], )
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('subjects_playwrights')
    op.drop_table('subjects_directors')
    op.drop_table('subjects_actors')
    op.drop_table('celebrities')
    ### end Alembic commands ###
