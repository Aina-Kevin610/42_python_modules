#!/usr/bin/env python3

from .dark_spellbook import dark_spell_allowed_ingredients


def validate_ingredients(ingredients: str) -> str:
    allowed_ingredient: list[str] = dark_spellbook.dark_spellbook_allowed_ingredients()

    if ingredients in allowed_ingredient:
        return f"{ingredients} - VALID"
    else:
        return f"{ingredients} - INVALID"
