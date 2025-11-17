# backend/app/models/persona_profile.py
from .user import db
from datetime import datetime
import json

class PersonaProfile(db.Model):
    __tablename__ = 'persona_profiles'

    id = db.Column(db.String(36), primary_key=True, default=db.ForeignKey('users.id'))
    tone_analysis = db.Column(db.JSON)  # {formality: 0.8, humor: 0.3, professionalism: 0.9}
    common_phrases = db.Column(db.JSON)  # ["Best regards", "Looking forward to", ...]
    writing_style = db.Column(db.String(50))  # 'formal', 'casual', 'technical'
    vocabulary_complexity = db.Column(db.Float, default=0.5)
    response_length_preference = db.Column(db.String(20), default='medium')  # short, medium, long
    embedding_model = db.Column(db.String(100), default='all-MiniLM-L6-v2')
    is_trained = db.Column(db.Boolean, default=False)
    training_data_count = db.Column(db.Integer, default=0)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_dict(self):
        return {
            'user_id': self.id,
            'tone_analysis': self.tone_analysis or {},
            'common_phrases': self.common_phrases or [],
            'writing_style': self.writing_style,
            'vocabulary_complexity': self.vocabulary_complexity,
            'response_length_preference': self.response_length_preference,
            'is_trained': self.is_trained,
            'training_data_count': self.training_data_count,
            'updated_at': self.updated_at.isoformat()
        }