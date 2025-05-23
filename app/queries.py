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


def select_all_youtube_desktop():
    """
    Пример запроса для проверки:
    Поиск запросов НА ТЕМУ "ютуб" ТОЛЬКО на десктопах
        SELECT COUNT(*) FROM yandex_images
        WHERE request LIKE '%ютуб%' OR request LIKE '%Ютуб%'
        OR request LIKE '%youtu%' OR request LIKE '%Youtu%' OR request LIKE '%YouTu%'
        GROUP BY platform
        HAVING platform='desktop'
    """
    with sync_engine.connect() as conn:
        res = conn.execute(
            text(
                "SELECT COUNT(*) FROM yandex_images \
                WHERE request LIKE '%ютуб%' OR request LIKE '%Ютуб%' \
                OR request LIKE '%youtu%' OR request LIKE '%Youtu%' OR request LIKE '%YouTu%' \
                GROUP BY platform \
                HAVING platform='desktop'"
            )
        )
        return res.scalar()


def select_only_youtube_touch():
    """
    Пример запроса для проверки:
    Поиск строк, содержащих ТОЛЬКО "ютуб" в запросах ТОЛЬКО на тачах
        SELECT COUNT(*) FROM yandex_images
        WHERE request LIKE '%ютуб%'
        GROUP BY platform
        HAVING platform='touch'
    """
    with sync_engine.connect() as conn:
        res = conn.execute(
            text(
                "SELECT COUNT(*) FROM yandex_images \
                WHERE request LIKE '%ютуб%' \
                GROUP BY platform \
                HAVING platform='touch'"
            )
        )
        return res.scalar()


def select_only_youtube():
    """
    Количество запросов (строка request), содержащих ТОЛЬКО слово "ютуб" на всех платформах
        SELECT platform, COUNT(request) AS count_request
        FROM yandex_images
        WHERE request LIKE '%ютуб%'
        GROUP BY platform
        ORDER BY count_request DESC
    """
    with sync_engine.connect() as conn:
        res = conn.execute(
            text(
                "SELECT platform, COUNT(request) AS count_request \
                FROM yandex_images \
                WHERE request LIKE '%ютуб%' \
                GROUP BY platform \
                ORDER BY count_request DESC"
            )
        )
        return res.all()


def select_all_youtube():
    """
    Количество запросов (строка request) НА ТЕМУ "ютуб" на всех платформах
        SELECT platform, COUNT(request) AS count_request
        FROM yandex_images
        WHERE (request LIKE '%ютуб%' OR request LIKE '%Ютуб%'
        OR request LIKE '%youtu%' OR request LIKE '%Youtu%' OR request LIKE '%YouTu%')
        GROUP BY platform
        ORDER BY count_request DESC
    """
    with sync_engine.connect() as conn:
        res = conn.execute(
            text(
                "SELECT platform, COUNT(request) AS count_request \
                FROM yandex_images \
                WHERE (request LIKE '%ютуб%' OR request LIKE '%Ютуб%' \
                OR request LIKE '%youtu%' OR request LIKE '%Youtu%' OR request LIKE '%YouTu%') \
                GROUP BY platform \
                ORDER BY count_request DESC"
            )
        )
        return res.all()
