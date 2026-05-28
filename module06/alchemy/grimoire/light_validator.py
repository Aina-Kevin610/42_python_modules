#!/usr/bin/env python3


def validate_ingredients(ingredients: str) -> str:
    from .light_spellbook import light_spellbook_allowed_ingredients

    allowed_ingredient: list[str] = light_spellbook_allowed_ingredients()
    if ingredients in allowed_ingredient:
        return f"{ingredients} - VALID"
    else:
        return f"{ingredients} - INVALID"
