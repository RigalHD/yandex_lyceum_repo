from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import BaseModel


class Department(BaseModel):
    __tablename__ = "departments"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    title: Mapped[str] = mapped_column()
    chief_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    members: Mapped[str] = mapped_column()
    email: Mapped[str] = mapped_column()

    department_chief = relationship("User", back_populates="chief_departments")
