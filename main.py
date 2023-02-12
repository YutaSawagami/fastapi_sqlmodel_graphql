import strawberry
from fastapi import FastAPI
from sqlmodel import select
from strawberry.fastapi import GraphQLRouter

from database import create_session
from hero import Hero
from query import Query

schema = strawberry.Schema(Query)
graphql_app = GraphQLRouter(schema)

app = FastAPI()
app.include_router(graphql_app, prefix="/graphql")


@app.on_event("startup")
def register_heros():
    """サーバー起動時にHeroを登録"""
    with create_session() as session:
        session.add_all(
            [
                Hero(name="Deadpond", secret_name="Dive Wilson"),
                Hero(name="Spider-Boy", secret_name="Pedro Parqueador"),
                Hero(name="Rusty-Man", secret_name="Tommy Sharp", age=48),
            ]
        )
        session.commit()


@app.on_event("shutdown")
def delete_heros():
    """サーバー終了時にHeroを削除"""
    with create_session() as session:
        statement = select(Hero)
        heros = session.exec(statement).all()
        for hero in heros:
            session.delete(hero)
        session.commit()
