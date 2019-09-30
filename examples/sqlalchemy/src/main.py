import os

from flask import Flask
from flask import jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('CONNECTION_STRING')
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=False, nullable=False)

    def __iter__(self):
        for key, value in self.__dict__.items():
            if not key.startswith('_'):
                yield (key, value)


@app.route('/users', methods=['GET'])
def users():
    return jsonify([dict(user) for user in User.query.all()])


if __name__ == '__main__':
    app.run(debug=True)
