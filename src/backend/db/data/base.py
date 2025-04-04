from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import MetaData


class BaseModel(DeclarativeBase):
    metadata = MetaData()
