"""'Create user table'

Migration ID: '9c10d9ea'
Revises:
Created at: '26/09/2019'
"""
import os

from playhouse.db_url import connect

# Nomade migration identifiers
migration_name = 'Create user table'
migration_date = '26/09/2019'
curr_migration = '9c10d9ea'
down_migration = None

db = connect(os.getenv('CONNECTION_STRING'))


def upgrade():
    """Write your upgrade statements here."""
    db.execute_sql(
        """
        create table user(
           id integer primary key,
           name varchar not null
        );
        """
    )

    for i in range(10):
        db.execute_sql(f'insert into user (name) values ("User {i}")')


def downgrade():
    """Write your downgrade statements here."""
    db.execute_sql('drop table user')
