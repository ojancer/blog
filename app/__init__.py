from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config  # Importa a classe de configuração

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    
    app.config.from_object(Config)  # Carrega tudo do config.py

    db.init_app(app)

    # Importa e registra as rotas (ainda vamos criar)
    from .routes import main
    from .admin_routes import admin

    app.register_blueprint(main)
    app.register_blueprint(admin, url_prefix='/admin')

    return app
