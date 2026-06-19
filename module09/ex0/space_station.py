#!/usr/bin/env python3
from pydantic import BaseModel, Field, ValidationError
from datetime import datetime


class SpaceStation(BaseModel):
    station_id: str = Field(..., min_length=3, max_length=10)
    name: str = Field(..., min_length=1, max_length=50)
    crew_size: int = Field(..., ge=1, le=20)
    power_level: float = Field(..., ge=0.0, le=100.0)
    oxygen_level: float = Field(..., ge=0.0, le=100.0)
    last_maintenance: datetime = Field(...)
    is_operational: bool = Field(default=True)
    notes: str | None = Field(default=None, max_length=200)


def main() -> None:
    print("Space Station Data Validation")

    valid = SpaceStation(
        station_id="ISS001",
        name="International Space Station",
        crew_size=6,
        power_level=85.5,
        oxygen_level=92.3,
        last_maintenance="2026-06-18T14:30:00",
        is_operational=True,
    )

    print("========================================")
    print("Valid station created:")
    print("ID:", valid.station_id)
    print("Name:", valid.name)
    print(f"Crew: {valid.crew_size} people")
    print(f"Power: {valid.power_level}%")
    print(f"Oxygen: {valid.oxygen_level}%")
    print("Status:", "Operational" if valid.is_operational else "Not Operational")
    print("========================================")

    try:
        invalid = SpaceStation(
            station_id="ISS001",
            name="International Space Station",
            crew_size=27,
            power_level=85.5,
            oxygen_level=92.3,
            last_maintenance="2026-06-18T14:30:00",
            is_operational=True,
        )
    except ValidationError as e:
        print("Expected validation error:")
        print(e.errors()[0]["msg"])


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print("Error - ", e)