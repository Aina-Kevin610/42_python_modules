def validate_ingredients(ingredients: str) -> str:
    from .light_spellbook import light_spell_allowed_ingredients
    allowed: list[str] = light_spell_allowed_ingredients()
    valid: bool = any(a.lower() in ingredients.lower() for a in allowed)
            
    return f"{ingredients} - {'VALID' if valid else 'INVALID'}"
