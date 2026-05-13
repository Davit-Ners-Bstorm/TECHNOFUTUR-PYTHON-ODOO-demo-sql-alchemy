from db.database import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, ForeignKey
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from models.user import Users

class Profiles(Base):
    __tablename__ = "profiles"

    id: Mapped[int] = mapped_column(primary_key=True)

    bio: Mapped[str] = mapped_column(String(500))

    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id"),
        unique=True,
        nullable=False
    )

    user: Mapped["Users"] = relationship(
        "Users",
        back_populates="profil"
    )

    def __repr__(self):
        return f'Profil : BIO : {self.bio}'
    

