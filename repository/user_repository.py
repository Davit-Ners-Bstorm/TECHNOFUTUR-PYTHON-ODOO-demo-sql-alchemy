from sqlalchemy.orm import Session, joinedload
from sqlalchemy import select
from models.user import Users

def create_user(session: Session, username: str, email: str, country: str):
    user = Users(username=username, email=email, country=country)

    session.add(user)
    session.commit()
    session.refresh(user)

    return user


def get_user_by_username(session: Session, username: str):
    stmt = select(Users).where(Users.username == username)
    user = session.execute(stmt).scalar_one_or_none()

    return user

def get_all_users(session: Session):
    stmt = select(Users)
    users = session.execute(stmt).scalars().all()

    return users

def get_all_users_with_profil(session: Session):
    stmt = (
        select(Users)
        .options(joinedload(Users.profil))
    )

    users = session.execute(stmt).scalars().all()

    return users

def get_all_users_with_profil_autre(session: Session):
    stmt = (
        select(Users)
        .join(Users.profil)
    )

    users = session.execute(stmt).scalars().all()

    return users

def update_user_country(session: Session, user_id: int, new_country: str):
    stmt = select(Users).where(Users.id == user_id)
    user = session.execute(stmt).scalar_one_or_none()

    if user is None:
        return None
    
    user.country = new_country
    session.commit()
    session.refresh(user)

    return user

def delete_user_by_id(session: Session, user_id):
    stmt = select(Users).where(Users.id == user_id)
    user = session.execute(stmt).scalar_one_or_none()

    if user is None:
        return False
    
    session.delete(user)
    session.commit()

    return True