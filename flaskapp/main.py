
from flask import Flask, jsonify, request
from .dao import get_games, insert_game, update_game, get_by_id, delete_game
from .db import create_tables

app = Flask(__name__)


@app.route("/games", methods=["POST"])
def create():
    game_details = request.get_json()
    name = game_details["name"]
    price = game_details["price"]
    rate = game_details["rate"]
    result = insert_game(name, price, rate)
    return jsonify(result)


@app.route("/games/<id>", methods=["GET"])
def get(id):
    game = get_by_id(id)
    return jsonify(game)


@app.route('/games', methods=["GET"])
def list():
    games = get_games()
    return jsonify(games)


@app.route("/games/<id>", methods=["PUT"])
def update():
    game_details = request.get_json()
    id = game_details["id"]
    name = game_details["name"]
    price = game_details["price"]
    rate = game_details["rate"]
    result = update_game(id, name, price, rate)
    return jsonify(result)


@app.route("/games/<id>", methods=["DELETE"])
def delete(id):
    result = delete_game(id)
    return jsonify(result)


def run():
    create_tables()
    app.run(host='0.0.0.0', port=8000, debug=False)
