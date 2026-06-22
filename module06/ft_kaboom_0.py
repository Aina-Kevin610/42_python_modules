#!/usr/bin/env python3

from alchemy.grimoire.light_spellbook import light_spell_record

if __name__ == "__main__":
    print("=== Kaboom 0 ===")
    print("Using grimoire module directly")
    result: str = light_spell_record("Fantasy", "Ehyt, wnd and fre")
    print(f"Testing record light spell: {result}")
