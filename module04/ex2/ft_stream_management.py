#!/usr/bin/env python3

import sys
import typing


class UsageError(Exception):
    pass


def main() -> None:
    file: IO[str] = None
    try:
        if len(sys.argv) != 2:
            raise UsageError("ft_ancient_text.py <file>")
        print(f"Accessing file '{sys.argv[1]}'")
        file = open(sys.argv[1], "r")
        content = file.read()
        print("---\n")
        print(content)
        print("\n---")
        file.close()
        sys.stdout.write(f"File '{sys.argv[1]}' closed.")
        print("\nTransform data:")
        contents = content.split("\n")
        new_content = []
        for content in contents:
            new_content.append(content + "#")
            print(content + '#')
        print("---\n")
        filename = input("Enter new file name (or empty): ")
        if filename == "":
            print("Not saving data.")
        else:
            file = open(filename, "w")
            for content in new_content:
                file.write(content + "\n")
            print(f"Saving data to '{filename}'\n"
                  f"Data saved in file '{filename}'")
        file.close()
    except UsageError as e:
        sys.stderr.write(f"[STDERR] Usage: {e}")
    except FileNotFoundError as e:
        sys.stderr.write(f"[STDERR] Error opening file '{sys.argv[1]}': {e}")
    except PermissionError as e:
        sys.stderr.write(f"[STDERR] Error opening file '{sys.argv[1]}': {e}")
    except EOFError as e:
        sys.stderr.write("[STDERR] Programm interupted")
    except Exception as e:
        sys.stderr.write("[STDERR] Programm interupted")
    finally:
        if not file is None:
            file.close()

if __name__ == "__main__":
    print("=== Cyber Archives Recovery & Preservation ===")
    main()