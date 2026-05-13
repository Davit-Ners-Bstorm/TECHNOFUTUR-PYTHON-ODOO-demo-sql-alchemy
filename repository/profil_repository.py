from sqlalchemy.orm import Session
from sqlalchemy import select
from models.profil import Profiles

def create_profil(session: Session, user_id: int, bio: str):
    profil = Profiles(user_id=user_id, bio=bio)

    session.add(profil)
    session.commit()
    session.refresh(profil)

    return profil