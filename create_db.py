from app import create_app, db
from app import models  # Isso garante que os models são registrados no SQLAlchemy

app = create_app()

with app.app_context():
    db.create_all()
    print("✅ Tabelas criadas com sucesso!")
