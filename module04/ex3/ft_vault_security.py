#!/usr/bin/env python3


def secure_archive(filename, mode="read", content=None):
    if mode == "write":
        try:
            with open(filename, "w") as f:
                f.write(content)
            return (True, "Content successfully written to file")
        except Exception as e:
            return (False, str(e))
    else:
        try:
            with open(filename, "r") as f:
                return (True, f.read())
        except Exception as e:
            return (False, str(e))


if __name__ == "__main__":
    print("=== Cyber Archives Security ===\n")
    print("Using 'secure_archive' to read from a nonexistent file:")
    print(secure_archive("/not/existing/file"))
    print("\n")
    print("Using 'secure_archive' to read from an inaccessible file:")
    print(secure_archive("/etc/shadow"))
    print("\n")
    print("Using 'secure_archive' to read from a regular file:")
    print(secure_archive("ancient_fragment.txt"))
    print("\n")
    result = secure_archive("archive.txt")
    print("Using 'secure_archive' to write previous content to a new file:")
    print(secure_archive("new_archive.txt", mode="write", content=result[1]))