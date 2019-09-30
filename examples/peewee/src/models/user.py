import os

import peewee as pw
from playhouse.db_url import connect

db = connect(os.getenv('CONNECTION_STRING'))


class User(pw.Model):
    id = pw.AutoField()
    name = pw.CharField()

    class Meta:
        database = db
