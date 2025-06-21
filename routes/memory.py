
from flask import Blueprint, jsonify

memory_bp = Blueprint('memory', __name__)

@memory_bp.route('/memory/<string:playerId>', methods=['GET'])
def get_memory(playerId):
    mock_memory = {
        "playerId": playerId,
        "entries": [
            "Refused Echo Priestess",
            "Fighting the Vault Guardian",
            "Carrying Hollow God's Curse"
        ]
    }
    return jsonify(mock_memory)
