from sqlalchemy import ForeignKey
import datetime
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy_serializer import SerializerMixin

from .base import BaseModel


class Jobs(BaseModel, SerializerMixin):
    __tablename__ = "jobs"

    serialize_rules = ("-leader", "-category", "-creator")

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    job: Mapped[str] = mapped_column()
    work_size: Mapped[int] = mapped_column()
    collaborators: Mapped[str] = mapped_column(nullable=True)
    start_date: Mapped[datetime.datetime] = mapped_column(default=datetime.datetime.now)
    end_date: Mapped[datetime.datetime] = mapped_column(nullable=True)
    is_finished: Mapped[bool] = mapped_column(default=False)

    team_leader: Mapped[int] = mapped_column(ForeignKey("users.id"))
    leader = relationship(
        "User", back_populates="jobs_leading", foreign_keys=[team_leader]
    )

    creator_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    creator = relationship(
        "User", back_populates="created_jobs", foreign_keys=[creator_id]
    )

    category_id: Mapped[int] = mapped_column(ForeignKey("jobs_categories.id"))
    category = relationship(
        "JobCategories", back_populates="jobs", foreign_keys=[category_id]
    )


class JobCategories(BaseModel):
    __tablename__ = "jobs_categories"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column()

    jobs: Mapped[list["Jobs"]] = relationship(back_populates="category")
