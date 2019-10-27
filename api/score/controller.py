from api import app
from flask import jsonify
from flask import request
from api.score import services as score_services


@app.route('/api/v1/score', methods=['POST'])
def calculate_score():
    data = request.get_json(force=True)
    rolls = data.get('rolls')
    if rolls is None:
        return jsonify({"message": "parameter \"rolls\" is required"}), 422
    try:
        score = score_services.calculate_score(rolls)
    except Exception as e:
        return jsonify({"message": "error"}, 500)
    return jsonify({'score': score})