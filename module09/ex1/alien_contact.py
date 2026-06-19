#!/usr/bin/env python3

from pydantic import BaseModel, Field, model_validator
from datetime import datetime
from enum import Enum
from typing import Self


class CheckError(Exception):
    pass


class ContactType(Enum):
    radio = "radio"
    visual = "visual"
    physical = "physical"
    telepathic = "telepathic"


class AlienContact(BaseModel):
    contact_id: str = Field(..., min_length=5, max_length=15)
    timestamp: datetime = Field(...)
    location: str = Field(..., min_length=3, max_length=100)
    contact_type: ContactType = Field(...)
    signal_strength: float = Field(..., ge=0.0, le=10.0)
    duration_minutes: int = Field(..., ge=1, le=1440)
    witness_count: int = Field(..., ge=1, le=100)
    message_received: str | None = Field(default=None)
    is_verified: bool = Field(default=False)

    @model_validator(mode="after")
    def validation_rules(self) -> Self:
        if not self.contact_id.startswith("AC"):
            raise CheckError("Contact_id must start with 'AC'")
        if not self.is_verified and self.contact_type == ContactType.physique:
            raise CheckError("Physical contact reports must be verified")
        if int(self.witness_count) < 3 and self.contact_type == ContactType.telepathic:
            raise CheckError("Telepathic contact requires at least 3 witnesses")
        if self.signal_strength > 7.0 and not self.message_received:
            raise ValueError('Strong signals (> 7.0) should include received messages')
        return self


def main() -> None:
    print("Alien Contact Log Validation")

    # Creating valid data for alien contact...
    valid = AlienContact(
        contact_id = "AC_2024_001",
        timestamp = "2026-06-18T14:30:00",
        location = "Area 51, Nevada",
        contact_type = ContactType.radio,
        signal_strength = "8.5",
        duration_minutes = "45",
        witness_count = "5",
        message_received = "Greetings from Zeta Reticuli",
        is_verified = True,
    )

    print("======================================")
    print("Valid contact report:")
    print("ID: ", valid.contact_id)
    print("Type: ", valid.contact_type)
    print("Location: ", valid.location)
    print("Signal: ", valid.signal_strength, "/10")
    print("Duration: ", valid.duration_minutes, "minutes")
    print("Witnesses: ", valid.witness_count)
    print("Message: ", valid.message_received)
    print("======================================")

    # Creating invalid data for alien contact witness_count < 3 with telepathic contact type...
    try:
        invalid = AlienContact(
            contact_id = "AC_2024_001",
            timestamp = "2026-06-18T14:30:00",
            location = "Area 51, Nevada",
            contact_type = ContactType.telepathic,
            signal_strength = "8.5",
            duration_minutes = "45",
            witness_count = 2,
            message_received = "Greetings from Zeta Reticuli",
            is_verified = True,
        )

        print("======================================")
        print("invalid contact report:")
        print("ID: ", invalid.contact_id)
        print("Type: ", invalid.contact_type)
        print("Location: ", invalid.location)
        print("Signal: ", invalid.signal_strength, "/10")
        print("Duration: ", invalid.duration_minutes, "minutes")
        print("Witnesses: ", invalid.witness_count)
        print("Message: ", invalid.message_received)
        print("======================================")
    except CheckError as e:
        print("Expected validation error:")
        print(e)

if __name__ == "__main__":
    try:
        main()
    except Exception:
        print("Something went wrong!")