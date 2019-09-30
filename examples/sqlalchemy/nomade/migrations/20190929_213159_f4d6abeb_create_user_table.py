"""Create user table

Migration ID: f4d6abeb
Revises:
Created at: 29/09/2019
"""
import os
import sys
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(current_dir, '..', '..'))

from src.main import db

# Nomade migration identifiers
migration_name = 'Create user table'
migration_date = '29/09/2019'
curr_migration = 'f4d6abeb'
down_migration = ''


def upgrade():
    """Write your upgrade statements here."""
    db.engine.execute(
        """
        CREATE TABLE user(
           id INTEGER AUTO_INCREMENT PRIMARY KEY,
           name VARCHAR(80) NOT NULL
        );
        """
    )

    for i in range(10):
        db.engine.execute(f'INSERT INTO user (name) VALUES ("User {i}")')


def downgrade():
    """Write your downgrade statements here."""
    db.engine.execute('DROP TABLES user')
