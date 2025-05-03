from .database import db
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import List, TYPE_CHECKING

if TYPE_CHECKING:
    from .planets import Planet
    from .favorite import Favorite

class People(db.Model):
    __tablename__ = "people"
    id: Mapped[int] = mapped_column(primary_key=True)
    person_name: Mapped[str] = mapped_column(
        String(120), unique=True, nullable=False)
    coalition: Mapped[str] = mapped_column(String(120), nullable=False)
    race: Mapped[str] = mapped_column(String(120), nullable=False)
    age: Mapped[int] = mapped_column(nullable=False)
    planets: Mapped['Planet'] = relationship(
        back_populates="person",
    )
    favorite: Mapped[List["Favorite"]] = relationship(
        back_populates="people",
    )