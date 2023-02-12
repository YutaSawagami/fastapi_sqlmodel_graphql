from typing import Optional

import strawberry
from sqlmodel import Field, SQLModel


class Hero(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    secret_name: str
    age: Optional[int] = None


@strawberry.experimental.pydantic.type(model=Hero, all_fields=True)
class HeroType:
    pass
