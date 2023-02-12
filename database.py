from sqlmodel import Session, create_engine

engine = create_engine("sqlite:///database.db")


def create_session():
    return Session(engine)
