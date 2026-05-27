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
        sys.stdout.write(f"File '{sys.argv[1]}' closed.\n")
        print("\nTransform data:")
        print("---\n")
        contents = content.split("\n")
        new_content = []
        for content in contents:
            new_content.append(content + "#")
            print(content + '#')
        print("\n---")
        sys.stdout.write("\nEnter new file name (or empty):")
        sys.stdout.flush()
        filename = sys.stdin.readline()
        if filename == "\n":
            print("Not saving data.")
        else:
            file = open(filename, "w")
            for content in new_content:
                file.write(content + "\n")
            print(f"Saving data to '{filename.replace("\n", "")}'")
            print(f"Data saved in file '{filename.replace("\n", "")}'")
    except UsageError as e:
        sys.stderr.write(f"[STDERR] Usage: {e}")
    except FileNotFoundError as e:
        sys.stderr.write(f"[STDERR] Error opening file '{sys.argv[1]}': {e}")
    except PermissionError as e:
        sys.stderr.write(f"[STDERR] Error opening file '{sys.argv[1]}': {e}")
    except EOFError:
        sys.stderr.write("[STDERR] Programm interupted")
    except Exception as e:
        sys.stderr.write(f"[STDERR] Programm interupted {e}")
    except IsADirectoryError:
        print(sys.argv[1], " is a directory")
    finally:
        if file is not None:
            file.close()


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
