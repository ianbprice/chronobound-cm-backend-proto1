
from flask import Flask
from routes.character import character_bp
from routes.memory import memory_bp
from routes.combat import combat_bp
from routes.image import image_bp

app = Flask(__name__)

app.register_blueprint(character_bp)
app.register_blueprint(memory_bp)
app.register_blueprint(combat_bp)
app.register_blueprint(image_bp)

@app.route('/')
def health():
    return {'status': 'ChronoBound API is alive'}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
