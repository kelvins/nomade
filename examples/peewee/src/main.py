from flask import Flask, jsonify
from playhouse.shortcuts import model_to_dict

from models.user import User

app = Flask(__name__)


@app.route('/users', methods=['GET'])
def users():
    return jsonify([model_to_dict(u) for u in User.select()])


if __name__ == '__main__':
    app.run(debug=True)
