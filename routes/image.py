
from flask import Blueprint, request, jsonify

image_bp = Blueprint('image', __name__)

@image_bp.route('/image/generate', methods=['POST'])
def generate_image():
    data = request.json
    prompt = data.get('description', '')
    style = data.get('style', 'cinematic')
    return jsonify({
        "image_url": f"https://dummyimage.com/600x400/000/fff&text={prompt.replace(' ', '+')}"
    })
