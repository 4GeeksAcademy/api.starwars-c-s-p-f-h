from.database import db
from sqlalchemy import Integer, String, Boolean 
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import List, TYPE_CHECKING

if TYPE_CHECKING:
    from .people import People
    from .favorite import Favorite

class Planet(db.Model):
    __tablename__ = "planets"
    id: Mapped[int] = mapped_column(primary_key=True)
    planet_name: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    film_appearance: Mapped[str] = mapped_column(String(120), nullable=False)
    exploted: Mapped[bool] = mapped_column(Boolean(), nullable=False)
    population: Mapped[int] = mapped_column(Integer(), nullable=False)
    people: Mapped[List["People"]] = relationship(
        back_populates="planets",
    )
    favorite: Mapped[List["Favorite"]] = relationship(
        back_populates="planets",
    )
    
    def serialize(self):
        return {
            'id' : self.id,
            'planet_name' : self.planet_name,
            'film_appearance' : self.film_appearance,
            'exploted' : self.exploted,
            'population': self.population
        }
    
    def serialize_with_relations(self):
        data = self.serialize()
        data['people'] = [people.serialize() for people in self.people]
        data['favorite'] = [favorite.serialize() for favorite in self.favorite]
        return data 
   