from sqlalchemy import select, text

from database import sync_engine
from models import YandexImages, Base


def create_tables():
    """
    Создание таблицы
    """
    sync_engine.echo = True
    # Base.metadata.drop_all(sync_engine)
    Base.metadata.create_all(sync_engine)


def select_count():
    """
    Количество строк в базе
    """
    with sync_engine.connect() as conn:
        res = conn.execute(text("SELECT COUNT (*) FROM yandex_images"))
        return res.scalar()


def select_id(n):
    """
    Строка по id
    """
    with sync_engine.connect() as conn:
        query = select(YandexImages).where(YandexImages.id == n)
        return conn.execute(query).first()


def get_date(n):
    """
    Дата по id
    """
    with sync_engine.connect() as conn:
        query = select(YandexImages.date).where(YandexImages.id == n)
        return conn.execute(query).scalar()


def select_min_date():
    """
    Ранняя запись
    """
    with sync_engine.connect() as conn:
        res = conn.execute(text("SELECT MIN(date) FROM yandex_images"))
        return res.scalar()


def select_max_date():
    """
    Ранняя запись
    """
    with sync_engine.connect() as conn:
        res = conn.execute(text("SELECT MAX(date) FROM yandex_images"))
        return res.scalar()


def select_youtube_desktop():
    """
    Поиск строк, содержащих слово "ютуб" (или Ютуб) в запросах на десктопах
        SELECT COUNT(*) FROM yandex_images
        WHERE request LIKE '%ютуб%' OR request LIKE '%Ютуб%'
        GROUP BY platform
        HAVING platform='desktop'
    """
    with sync_engine.connect() as conn:
        res = conn.execute(
            text(
                "SELECT COUNT(*) FROM yandex_images \
                WHERE request LIKE '%ютуб%' OR request LIKE '%Ютуб%' \
                GROUP BY platform \
                HAVING platform='desktop'"
            )
        )
        return res.scalar()


def select_youtube_touch():
    """
    Поиск строк, содержащих слово "ютуб" (или Ютуб) в запросах на тачах
        SELECT COUNT(*) FROM yandex_images
        WHERE request LIKE '%ютуб%' OR request LIKE '%Ютуб%'
        GROUP BY platform
        HAVING platform='touch'
    """
    with sync_engine.connect() as conn:
        res = conn.execute(
            text(
                "SELECT COUNT(*) FROM yandex_images \
                WHERE request LIKE '%ютуб%' OR request LIKE '%Ютуб%' \
                GROUP BY platform \
                HAVING platform='touch'"
            )
        )
        return res.scalar()
