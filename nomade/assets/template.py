"""{migration_name}

Migration ID: {curr_migration}
Revises: {down_migration}
Created at: {migration_date}
"""

# Nomade migration identifiers
migration_name = '{migration_name}'
migration_date = '{migration_date}'
curr_migration = '{curr_migration}'
down_migration = '{down_migration}'


def upgrade():
    """Write your upgrade statements here."""


def downgrade():
    """Write your downgrade statements here."""
