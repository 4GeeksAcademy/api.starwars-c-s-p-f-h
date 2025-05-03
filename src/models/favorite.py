from .database import db
from sqlalchemy import  ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .user import User
    from .planets import Planet
    from .people import People

class Favorite(db.Model):
    __tablename__ = "favoritos"
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id:Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    planet_id:Mapped[int] = mapped_column(ForeignKey("planets.id"), nullable=True)
    pperson_id:Mapped[int] = mapped_column(ForeignKey("people.id"), nullable=True)    
    user: Mapped['User'] = relationship(
        back_populates="favorite",
    )
    people: Mapped['People'] = relationship(
        back_populates="favorite",
    )
    planets: Mapped['Planet'] = relationship(
        back_populates="favorite",
    )