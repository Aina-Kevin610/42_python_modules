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
        file: IO[str] = open(sys.argv[1], "r")
        content = file.read()
        print("---\n")
        print(content)
        print("\n---")
        file.close()
        print(f"File '{sys.argv[1]}' closed.")
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
            file.close()
            file: IO[str] = open(filename, "w")
            for content in new_content:
                file.write(content + "\n")
            print(f"Saving data to '{filename}'\n"
                  f"Data saved in file '{filename}'")
    except UsageError as e:
        print(f"Usage: {e}")
    except FileNotFoundError as e:
        print(f"Error opening file '{sys.argv[1]}': {e}")
    except PermissionError as e:
        print(f"Error opening file '{sys.argv[1]}': {e}")
    except EOFError as e:
        print("Programm interupted")
    except Exception:
        print("Programm interupted")
        
if __name__ == "__main__":
    print("=== Cyber Archives Recovery & Preservation ===")
    main()