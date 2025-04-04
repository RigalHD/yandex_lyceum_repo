import sqlalchemy as sa
import sqlalchemy.orm as orm

from .base import BaseModel

__factory = None


def global_init(db_file: str, drop_db: bool = False) -> None:
    global __factory

    if __factory:
        return

    if not db_file or not db_file.strip():
        raise Exception("Необходимо указать файл базы данных.")

    conn_str = f"sqlite:///{db_file.strip()}?check_same_thread=False"
    print(f"Подключение к базе данных по адресу {conn_str}")

    engine = sa.create_engine(conn_str, echo=False)
    __factory = orm.sessionmaker(bind=engine)

    if drop_db is True:
        BaseModel.metadata.drop_all(engine)

    BaseModel.metadata.create_all(engine)


def create_session() -> orm.Session:
    global __factory
    return __factory()
