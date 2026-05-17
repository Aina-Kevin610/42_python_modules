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
        print("---\n")
        print(file.read())
        print("\n---")
    except UsageError as e:
        print(f"Usage: {e}")
        return
    except FileNotFoundError as e:
        print(f"Error opening file '{sys.argv[1]}': {e}")
        return
    except PermissionError as e:
        print(f"Error opening file '{sys.argv[1]}': {e}")
        return
    finally:
        if file is None:
            return
        file.close()
        print(f"File '{sys.argv[1]}' closed.")


if __name__ == "__main__":
    print("=== Cyber Archives Recovery ===")
    main()