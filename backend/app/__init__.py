# backend/app/__init__.py
from flask import Flask
from flask_migrate import Migrate
from app.config import config
from app.models import db, bcrypt
from app.auth.jwt import jwt

def create_app(config_name='default'):
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    # Initialize extensions
    db.init_app(app)
    bcrypt.init_app(app)
    jwt.init_app(app)
    Migrate(app, db)

    # Register blueprints
    from app.auth import auth_bp
    app.register_blueprint(auth_bp, url_prefix='/api/auth')

    # Health check route
    @app.route('/health')
    def health_check():
        return jsonify({'status': 'healthy', 'service': 'AI Persona Clone API'})

    return app