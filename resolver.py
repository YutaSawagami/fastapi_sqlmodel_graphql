from sqlmodel import select

from database import create_session
from hero import Hero


def get_heros():
    """ヒーローの一覧を返す."""
    with create_session() as session:
        statement = select(Hero)
        return session.exec(statement).all()


def get_hero_by_id(id: int):
    """idを基にヒーローを返す."""
    with create_session() as session:
        statement = select(Hero).filter(Hero.id == id)
        return session.exec(statement).first()
