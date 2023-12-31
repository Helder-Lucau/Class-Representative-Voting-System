"""Added vote  model

Revision ID: 4a58d9f15984
Revises: 5848c616f236
Create Date: 2023-09-08 02:39:37.210808

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '4a58d9f15984'
down_revision: Union[str, None] = '5848c616f236'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('votes',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('voter_id', sa.Integer(), nullable=True),
    sa.Column('candidate_id', sa.Integer(), nullable=True),
    sa.Column('vote_count', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['candidate_id'], ['candidates.id'], ),
    sa.ForeignKeyConstraint(['voter_id'], ['voters.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('votes')
    # ### end Alembic commands ###
