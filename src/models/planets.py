from .database import db
from sqlalchemy import Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import List, TYPE_CHECKING

if TYPE_CHECKING:
    from .people import People
    from .favorite import Favorite

class Planet(db.Model):
    __tablename__ = "planets"
    planet_id: Mapped[int] = mapped_column(primary_key=True)
    planet_name: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    film_appearance: Mapped[str] = mapped_column(String(120), nullable=False)
    exploted: Mapped[bool] = mapped_column(Boolean(), nullable=False)
    population: Mapped[int] = mapped_column(Integer(), nullable=False)
    # people_id: Mapped[int] = mapped_column(ForeignKey("peoples.id", nullable=True))
    people: Mapped[List["People"]] = relationship(
        back_populates="planet",
    )
    favorite: Mapped[List["Favorite"]] = relationship(
        back_populates="planets",
    )
    
    def serialize(self):
        return {
            'id' : self.id,
            'planet_name' : self.planet_name,
            'population': self.population
        }
    
    