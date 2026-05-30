import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent / '..' / 'backend'))
from app.core.database import Base, engine, SessionLocal
from app.core import models
from app.core.security import get_password_hash


def seed():
    Base.metadata.create_all(bind=engine)
    db = SessionLocal()
    if not db.query(models.User).filter(models.User.email == 'admin@campusgpt.ai').first():
        admin = models.User(
            email='admin@campusgpt.ai',
            full_name='CampusGPT Admin',
            role='admin',
            hashed_password=get_password_hash('Admin@123'),
        )
        db.add(admin)
        db.commit()
    db.close()

if __name__ == '__main__':
    seed()
    print('Database seeded with admin user.')
