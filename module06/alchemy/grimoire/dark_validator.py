#!/usr/bin/env python3

from .dark_spellbook import dark_spell_allowed_ingredients


def validate_ingredients(ingredients: str) -> str:
    allowed: list[str] = dark_spell_allowed_ingredients()
    valid: bool = any(a.lower() in ingredients.lower() for a in allowed)
    return f"{ingredients} - {'VALID' if valid else 'INVALID'}"
