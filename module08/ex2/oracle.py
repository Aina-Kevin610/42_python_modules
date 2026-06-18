import os
import sys

try:
    from dotenv import load_dotenv
except ImportError:
    print("ERROR: python-dotenv is not installed.")
    sys.exit(1)


class ConfigError(Exception):
    pass


def main() -> None:
    print("ORACLE STATUS: Reading the Matrix...\n")

    required_keys = [
        "MATRIX_MODE",
        "DATABASE_URL",
        "API_KEY",
        "LOG_LEVEL",
        "ZION_ENDPOINT"
        ]

    overridden = any(key in os.environ for key in required_keys)
    env_exists = os.path.exists(".env")

    load_dotenv()

    matrix_mode = os.getenv("MATRIX_MODE")
    db_url = os.getenv("DATABASE_URL")
    api_key = os.getenv("API_KEY")
    log_level = os.getenv("LOG_LEVEL")
    zion_endpoint = os.getenv("ZION_ENDPOINT")

    print("Configuration loaded:")
    print(f"Mode: {matrix_mode}")
    print(f"Database: {db_url}")
    print(f"API Access: {api_key}")
    print(f"Log Level: {log_level}")
    print(f"Zion Network: {zion_endpoint}\n")

    print("Environment security check:")

    try:
        if not api_key or not db_url:
            print("[KO] Secrets are probably hardcoded!")
        else:
            print("[OK] No hardcoded secrets detected")

        if env_exists:
            print("[OK] .env file properly configured")
        else:
            print("[KO] No .env file detected")

        if overridden:
            print("[OK] Production overrides available")
        else:
            print("[KO] No overrides detected")

        if matrix_mode not in ["development", "production"]:
            raise ConfigError("[KO] MODE :('development' or 'production')")

        print("\nThe Oracle sees all configurations.")

    except ConfigError as e:
        print(e)
        sys.exit(1)


if __name__ == "__main__":
    main()
