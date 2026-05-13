from db.database import Base, engine
from sqlalchemy.orm import sessionmaker
from models.user import Users
from models.profil import Profiles
from repository.user_repository import create_user, get_all_users_with_profil_autre, get_user_by_username, get_all_users, get_all_users_with_profil, update_user_country
from repository.profil_repository import create_profil

Base.metadata.create_all(engine)

SessionLocal = sessionmaker(bind=engine)

with SessionLocal() as session:
    # Create a profil for an user by his user_id
    # profil = create_profil(session, 1, 'Bonjour, je suis Khun.')
    # print(profil)

    # Return one user by username
    # user = get_user_by_username(session, 'Khun')
    # print(user.profil)

    # # Return list de users
    # users = get_all_users(session)
    # print(users)

    # Return all users with profil
    # users_with_profil = get_all_users_with_profil(session)
    # print(users_with_profil[0])

    # Return all users with profil v2
    # users_with_profil = get_all_users_with_profil_autre(session)
    # print(users_with_profil[0])

    user_with_new_country = update_user_country(session, 1, 'USA')
    print(user_with_new_country)
