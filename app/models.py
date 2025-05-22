import datetime

from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase
from sqlalchemy.sql.sqltypes import DateTime


class Base(DeclarativeBase):
    pass


class YandexImages(Base):
    __tablename__ = "yandex_images"

    id: Mapped[int] = mapped_column(primary_key=True)
    request: Mapped[str] = mapped_column()
    date: Mapped[datetime.datetime] = mapped_column(DateTime)
    platform: Mapped[str] = mapped_column()
