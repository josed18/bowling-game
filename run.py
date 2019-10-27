from api import app
from flask import jsonify
from api.utils import requesthandler

from api.score import controller


@app.route('/', methods=['GET'])
def main():
    return jsonify({
        'status': "ok",
        'api': 'bowling-game'
    })


if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port='8080'
    )