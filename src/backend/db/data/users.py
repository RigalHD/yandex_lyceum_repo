import datetime
from flask_login import UserMixin
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy_serializer import SerializerMixin
from werkzeug.security import generate_password_hash, check_password_hash

from .base import BaseModel


class User(BaseModel, UserMixin, SerializerMixin):
    __tablename__ = "users"

    serialize_rules = ("-related_models.user.name",)

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    surname: Mapped[str] = mapped_column(nullable=True)
    name: Mapped[str] = mapped_column(nullable=True)
    age: Mapped[int] = mapped_column(nullable=True)
    position: Mapped[str] = mapped_column(nullable=True)
    speciality: Mapped[str] = mapped_column(nullable=True)
    address: Mapped[str] = mapped_column(nullable=True)
    email: Mapped[str] = mapped_column(unique=True)
    hashed_password: Mapped[str] = mapped_column(nullable=True)
    modified_date: Mapped[datetime.datetime] = mapped_column(
        default=datetime.datetime.now
    )

    jobs_leading: Mapped[list["Jobs"]] = relationship(  # type: ignore
        back_populates="leader",
        uselist=True,
        lazy="selectin",
        foreign_keys="Jobs.team_leader",
    )

    created_jobs: Mapped[list["Jobs"]] = relationship(  # type: ignore
        back_populates="creator",
        uselist=True,
        lazy="selectin",
        foreign_keys="Jobs.creator_id",
    )

    chief_departments: Mapped[list["Department"]] = relationship(  # type: ignore
        back_populates="department_chief",
        uselist=True,
        lazy="selectin",
        foreign_keys="Department.chief_id",
    )

    def get_id(self):
        return self.id

    def set_password(self, password):
        self.hashed_password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.hashed_password, password)
