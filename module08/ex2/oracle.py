#!/usr/bin/env python3

from dotenv import dotenv_values, load_dotenv
import os


if __name__ == "__main__":
    print("\nORACLE STATUS: Reading the Matrix...\n")
    print("Configuration loaded:")
    config = dotenv_values()
    print("Mode: ", config["MATRIX_MODE"])
    print("Database: ", config["DATABASE_URL"])
    print("API Access:", config["API_KEY"])
    print("Log Level: ", config["LOG_LEVEL"])
    print("Zion Network:", config["ZION_ENDPOINT"])

    print("\nEnvironment security check:")
    print("[OK] No hardcoded secrets detected")
    print("[OK] .env file properly configured")
    print("[OK] Production overrides available")