# backend/app/models/user_text.py
from .user import db, generate_uuid
from datetime import datetime

class UserText(db.Model):
    __tablename__ = 'user_texts'

    id = db.Column(db.String(36), primary_key=True, default=generate_uuid)
    user_id = db.Column(db.String(36), db.ForeignKey('users.id'), nullable=False, index=True)
    content = db.Column(db.Text, nullable=False)
    source_type = db.Column(db.String(50))  # 'email', 'chat', 'social', 'document'
    metadata = db.Column(db.JSON)  # {sender: '', recipient: '', platform: '', timestamp: ''}
    word_count = db.Column(db.Integer)
    is_processed = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'content': self.content,
            'source_type': self.source_type,
            'metadata': self.metadata or {},
            'word_count': self.word_count,
            'is_processed': self.is_processed,
            'created_at': self.created_at.isoformat()
        }