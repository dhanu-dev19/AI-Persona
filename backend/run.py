# backend/run.py
import os
from app import create_app
from app.models import db
from dotenv import load_dotenv

load_dotenv()

app = create_app(os.getenv('FLASK_CONFIG') or 'default')

# Create tables manually
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)