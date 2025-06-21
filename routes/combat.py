
import random
from flask import Blueprint, jsonify

combat_bp = Blueprint('combat', __name__)

@combat_bp.route('/combat/initiate', methods=['POST'])
def initiate_combat():
    initiative = random.randint(1, 20)
    return jsonify({
        "initiative": initiative,
        "narration": f"You rolled a {initiative}. The battle begins."
    })
