#!/usr/bin/env python3

import sys


class UsageError(Exception):
    pass


def main() -> None:
    file = None
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
            file = open(filename, "w")
            for content in new_content:
                file.write(content + "\n")
            print(f"Saving data to '{filename}'\n"
                  f"Data saved in file '{filename}'")
        file.close()
    except UsageError as e:
        print(f"Usage: {e}")
    except FileNotFoundError as e:
        print(f"Error opening file '{sys.argv[1]}': {e}")
    except PermissionError as e:
        print(f"Error opening file '{sys.argv[1]}': {e}")
    except IsADirectoryError:
        print(sys.argv[1], " is a directory")
    except EOFError:
        print("Programm interupted")
    except Exception:
        print("Programm interupted")


if __name__ == "__main__":
    print("=== Cyber Archives Recovery & Preservation ===")
    try:
        main()
    except Exception:
        print("Unknown error")
    except BaseException:
        print("Unknown error")
    except RuntimeError:
        print("Unknown error")
