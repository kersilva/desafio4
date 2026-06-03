from flask import Flask
from dotenv import load_dotenv
from src.views.routes import main_bp

load_dotenv()

app = Flask(__name__)
app.secret_key = 'uma_chave_secreta_bem_segura_aqui'

app.register_blueprint(main_bp)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)