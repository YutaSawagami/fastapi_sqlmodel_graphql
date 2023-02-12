from typing import Optional

import strawberry

from hero import HeroType
from resolver import get_hero_by_id, get_heros


@strawberry.type
class Query:
    heros: list[HeroType] = strawberry.field(resolver=get_heros)
    hero: Optional[HeroType] = strawberry.field(resolver=get_hero_by_id)
