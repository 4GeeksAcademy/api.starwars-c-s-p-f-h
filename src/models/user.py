from .database import db
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Boolean, Integer
from typing import List, TYPE_CHECKING

if TYPE_CHECKING:
    from .favorite import Favorite


class User(db.Model):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    email: Mapped[str] = mapped_column(
        String(120), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean(), nullable=False)
    favorite: Mapped[List["Favorite"]] = relationship(
        back_populates="user"
    )

    def serialize(self):
        return{
        "id":self.id,
        "name":self.name,
        "email":self.email,
        "is_active":self.is_active
    }
    def serialize_with_relations(self):
         data = self.serialize()
         data['favorites'] = [favorite.serialize() for favorite in self.favorite]
         return data
