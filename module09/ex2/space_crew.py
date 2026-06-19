#!/usr/bin/env python3

from pydantic import BaseModel, model_validator, Field
from enum import Enum
from datetime import datetime


class CheckError(Exception):
    pass


class CrewRank(Enum):
    cadet = "cadet"
    officer = "officer"
    lieutenant = "lieutenant"
    captain = "captain"
    commander = "commander"


class CrewMember(BaseModel):
    member_id: str = Field(..., min_length=3, max_length=10)
    name: str = Field(...,  min_length=2, max_length=50)
    rank: CrewRank = Field(...)
    age: int = Field(..., ge=18, le=80)
    specialization: str = Field(..., min_length=3, max_length=30)
    years_experience: int = Field(..., ge=0, le=50)
    is_active: bool = Field(default=True)


class SpaceMission(BaseModel):
    mission_id: str = Field(..., min_length=5, max_length=15)
    mission_name: str = Field(..., min_length=3, max_length=100)
    destination: str = Field(..., min_length=3, max_length=50)
    launch_date: datetime = Field(...)
    duration_days: int = Field(..., ge=1, le=3650)
    crew: list[CrewMember] = Field(..., min_length=1, max_length=12)
    mission_status: str = Field(default="planned")
    budget_millions: float = Field(..., ge=1.0, le=10000.0)

    @model_validator(mode="after")
    def validation_rules(self):
        if not self.mission_id.startswith("M"):
            raise CheckError("Mission ID must start with 'M'")
        
        if ("commander" or "captain") not in self.crew:
            raise CheckError("Must have at least one Commander or Captain")
        
        if self.duration_days > 365 and not any([crew for crew in self.crew if self.crew.years_experience >= 5]):
            raise CheckError("Long missions (> 365 days) need 50% experienced crew (5+ years)")

        if not all([status for status in self.crew.is_active]):
            raise CheckError("All crew members must be active")
        

if __name__ == "__main__":
    from datetime import datetime
    from pydantic import ValidationError

    print("Space Mission Crew Validation")
    
    # Creating a valid data...
    cmd_sarah = CrewMember(
        member_id="CREW01",
        name="Sarah Connor",
        rank=CrewRank.commander,
        age=45,
        specialization="Mission Command",
        years_experience=15,
        is_active=True
    )
    
    lt_john = CrewMember(
        member_id="CREW02",
        name="John Smith",
        rank=CrewRank.lieutenant,
        age=32,
        specialization="Navigation",
        years_experience=8,
        is_active=True
    )
    
    off_alice = CrewMember(
        member_id="CREW03",
        name="Alice Johnson",
        rank=CrewRank.officer,
        age=28,
        specialization="Engineering",
        years_experience=6,
        is_active=True
    )

    print("=========================================")
    mission_valid = SpaceMission(
        mission_id="M2024_MARS",
        mission_name="Mars Colony Establishment",
        destination="Mars",
        launch_date=datetime(2026, 6, 19),
        duration_days=900,
        crew=[cmd_sarah, lt_john, off_alice],
        budget_millions=2500.0
    )
    
    print("Valid mission created:")
    print(f"Mission: {mission_valid.mission_name}")
    print(f"ID: {mission_valid.mission_id}")
    print(f"Destination: {mission_valid.destination}")
    print(f"Duration: {mission_valid.duration_days} days")
    print(f"Budget: ${mission_valid.budget_millions}M")
    print(f"Crew size: {len(mission_valid.crew)}")
    print("Crew members:")
    for member in mission_valid.crew:
        print(f"- {member.name} ({member.rank.value}) - {member.specialization}")


    print("=========================================")
    print("Expected validation error:")
    
    cadet_tom = CrewMember(
        member_id="CREW04",
        name="Tom Spacey",
        rank=CrewRank.cadet,
        age=20,
        specialization="Systems",
        years_experience=1,
        is_active=True
    )

    # Creating an invalid data...
    try:
        mission_invalid = SpaceMission(
            mission_id="M2026_TEST",
            mission_name="Lunar Scouting",
            destination="Moon",
            launch_date=datetime(2026, 8, 1),
            duration_days=30,
            crew=[cadet_tom, lt_john],
            budget_millions=150.0
        )
    except ValidationError as e:
        print("Expected validation error:")
        print(e)