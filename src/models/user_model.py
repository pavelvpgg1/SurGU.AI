from sqlalchemy import String, Text
from sqlalchemy.orm import Mapped, mapped_column

from .base_model import Base


class UserModel(Base):
    __tablename__ = "users"

    id: Mapped[str] = mapped_column(String, primary_key=True)
    name: Mapped[str] = mapped_column(String)
    is_man: Mapped[bool]
    age: Mapped[int]
    dialog: Mapped[str] = mapped_column(Text)
