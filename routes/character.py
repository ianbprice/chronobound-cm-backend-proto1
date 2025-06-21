
from flask import Blueprint, request, jsonify

character_bp = Blueprint('character', __name__)

@character_bp.route('/character/create', methods=['POST'])
def create_character():
    data = request.json
    return jsonify({
        "status": "Character created",
        "character": data
    })
