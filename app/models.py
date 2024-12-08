from sqlalchemy.orm import Mapped, mapped_column
from flask_login import LoginManager, UserMixin  # noqa: F401
from app import db


class User(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(unique=True, nullable=False)
    email: Mapped[str] = mapped_column(unique=True, nullable=False,)
    password: Mapped[str] = mapped_column(nullable=False)
    role: Mapped[str] = mapped_column(default='User')  # Roles: 'Adrmin', 'User' # noqa: E501

    def __str__(self):
        return self.role == 'Adrmin'
