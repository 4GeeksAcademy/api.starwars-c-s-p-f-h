from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import List

db = SQLAlchemy()


class User(db.Model):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    email: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean(), nullable=False)
    favorite: Mapped[List["Favorite"]] = relationship(
        back_populates="users"
    )
    


class Planet(db.Model):
    __tablename__ = "planets"
    id: Mapped[int] = mapped_column(primary_key=True)
    planet_name: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    film_appearance: Mapped[str] = mapped_column(String(120), nullable=False)
    exploted: Mapped[bool] = mapped_column(Boolean(), nullable=False)
    population: Mapped[int] = mapped_column(Integer(), nullable=False)
    people_id:Mapped[int] = mapped_column(ForeignKey("peoples.id"), nullable=True)    
    people: Mapped[List["People"]] = relationship(
        back_populates="planets",
    )
    favorite_planet: Mapped[List["Favorite"]] = relationship(
        back_populates="planets",
    )

class People(db.Model):
    __tablename__ = "peoples"
    id: Mapped[int] = mapped_column(primary_key=True)
    person_name: Mapped[str] = mapped_column(
        String(120), unique=True, nullable=False)
    coalition: Mapped[str] = mapped_column(String(120), nullable=False)
    race: Mapped[str] = mapped_column(String(120), nullable=False)
    age: Mapped[int] = mapped_column(nullable=False)
    planet: Mapped["Planet"] = relationship(
        back_populates="peoples",
    )
    favorite_people: Mapped[List["Favorite"]] = relationship(
        back_populates="peoples",
    )


class Favorite(db.Model):
    __tablename__ = "favorites"
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id:Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    planet_id:Mapped[int] = mapped_column(ForeignKey("planets.id"), nullable=True)
    people_id:Mapped[int] = mapped_column(ForeignKey("peoples.id"), nullable=True)    
    """ favorite_user: Mapped["User"] = relationship(
        back_populates="favorites",
    ) """
    favorite_people: Mapped["People"] = relationship(
        back_populates="favorites",
    )
    favorite_planet: Mapped["Planet"] = relationship(
        back_populates="favorites",
    )


"""   def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        } """
