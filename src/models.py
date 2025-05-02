from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import List

db = SQLAlchemy()


class User(db.Model):
    __tablename__ = "users"
    user_id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean(), nullable=False)
    favoritos: Mapped[List["Favorito"]] = relationship(
        back_populates="User"
    )
    


class Planeta(db.Model):
    __tablename__ = "planetas"
    planeta_id: Mapped[int] = mapped_column(primary_key=True)
    planet_name: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    film_appearance: Mapped[str] = mapped_column(String(120), nullable=False)
    exploted: Mapped[bool] = mapped_column(Boolean(), nullable=False)
    population: Mapped[int] = mapped_column(Integer(), nullable=False)
    personaje_id:Mapped[int] = mapped_column(ForeignKey("personajes.personaje_id"), nullable=True)    
    personaje: Mapped[List["Personaje"]] = relationship(
        back_populates="planetas",
    )
    favoritos: Mapped[List["Favorito"]] = relationship(
        back_populates="planetas",
    )

class Personaje(db.Model):
    __tablename__ = "personajes"
    personaje_id: Mapped[int] = mapped_column(primary_key=True)
    person_name: Mapped[str] = mapped_column(
        String(120), unique=True, nullable=False)
    coalition: Mapped[str] = mapped_column(String(120), nullable=False)
    race: Mapped[str] = mapped_column(String(120), nullable=False)
    age: Mapped[int] = mapped_column(nullable=False)
    planeta: Mapped['Planeta'] = relationship(
        back_populates="personaje",
    )
    favoritos: Mapped[List["Favorito"]] = relationship(
        back_populates="personaje",
    )


class Favorito(db.Model):
    __tablename__ = "favoritos"
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id:Mapped[int] = mapped_column(ForeignKey("users.user_id"), nullable=False)
    planeta_id:Mapped[int] = mapped_column(ForeignKey("planetas.planeta_id"), nullable=True)
    personaje_id:Mapped[int] = mapped_column(ForeignKey("personajes.personaje_id"), nullable=True)    
    favorite: Mapped['User'] = relationship(
        back_populates="favorito",
    )
    favorite_person: Mapped['Personaje'] = relationship(
        back_populates="favorito",
    )
    favorite_planet: Mapped['Planeta'] = relationship(
        back_populates="favorito",
    )


"""   def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        } """
