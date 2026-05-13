from db.database import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from models.profil import Profiles


class Users(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)

    username: Mapped[str] = mapped_column(
        String(50),
        unique=True,
        nullable=False
    )

    email: Mapped[str] = mapped_column(
        String(50),
        unique=True
    )

    country: Mapped[str] = mapped_column(
        String(50),
    )

    profil: Mapped["Profiles"] = relationship(
        "Profiles",
        back_populates="user",
        uselist=False
    )

    def __repr__(self):
        return f'User : ID : {self.id} USERNAME : {self.username} EMAIL : {self.email} COUNTRY : {self.country} PROFIL : {self.profil}'
