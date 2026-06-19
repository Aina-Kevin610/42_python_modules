#!/usr/bin/env python3

from pytdantic import BaseModel, model_validator, Field
from enum import Enum
from datetime import datetime


class CheckError(Exception):
    pass


class CrewRank(Enum):
    cadet = "cadet"
    officier = "officier"
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
            raise CheckError("Long missions (> 365 days) need 50\% \experienced crew (5+ years)")

        if all([status for status in self.crew.is_active]):
            raise CheckError("All crew members must be active")
        

if __name__ == "__main__":
    