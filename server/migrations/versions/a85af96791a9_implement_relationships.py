"""implement relationships

Revision ID: a85af96791a9
Revises: bf1fe8bc8e8f
Create Date: 2024-07-31 17:51:34.524452

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a85af96791a9'
down_revision = 'bf1fe8bc8e8f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('signups', sa.Column('camper_id', sa.Integer(), nullable=True))
    op.add_column('signups', sa.Column('activity_id', sa.Integer(), nullable=True))
    op.create_foreign_key(op.f('fk_signups_activity_id_activities'), 'signups', 'activities', ['activity_id'], ['id'])
    op.create_foreign_key(op.f('fk_signups_camper_id_campers'), 'signups', 'campers', ['camper_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(op.f('fk_signups_camper_id_campers'), 'signups', type_='foreignkey')
    op.drop_constraint(op.f('fk_signups_activity_id_activities'), 'signups', type_='foreignkey')
    op.drop_column('signups', 'activity_id')
    op.drop_column('signups', 'camper_id')
    # ### end Alembic commands ###
