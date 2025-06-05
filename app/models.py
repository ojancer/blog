from datetime import datetime
from . import db

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(100), nullable=False)
    conteudo = db.Column(db.Text, nullable=False)
    data_criacao = db.Column(db.DateTime, default=datetime.utcnow)
    autor = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f'<Post {self.titulo}>'
