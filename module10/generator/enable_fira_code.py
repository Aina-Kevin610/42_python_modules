#!/usr/bin/env python3
import json
import shutil
from pathlib import Path

def main():
    user_settings = Path.home() / ".config" / "Code" / "User" / "settings.json"
    backup = user_settings.parent / (user_settings.name + ".bak")

    # Ensure parent dir exists
    user_settings.parent.mkdir(parents=True, exist_ok=True)

    if user_settings.exists():
        shutil.copy2(user_settings, backup)
        try:
            data = json.loads(user_settings.read_text(encoding='utf-8'))
        except Exception:
            data = {}
    else:
        data = {}

    # Merge desired settings
    data.update({
        "editor.fontFamily": "'Fira Code', Consolas, 'Courier New', monospace",
        "editor.fontLigatures": True
    })

    user_settings.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding='utf-8')
    print(f"Updated {user_settings}")
    if backup.exists():
        print(f"Backup saved to {backup}")

if __name__ == '__main__':
    main()
