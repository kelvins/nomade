"""{migration_name} ({migration_date})

Migration {curr_migration} revises {down_migration}.
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
