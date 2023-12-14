from pydantic import BaseModel, Field
from datetime import datetime


class TeamStat(BaseModel):
    teamName: str
    matchPlayed: int
    points: int
    updated_on: datetime = Field(default=datetime.now())


class TeamStatGoals(BaseModel):
    teamName: str
    goals: int
    updated_on: datetime = Field(default=datetime.now())


class PlayerStat(BaseModel):
    playerName: str
    teamName: str
    goals: int
    updated_on: datetime = Field(default=datetime.now())


class TeamStatsResponseModal(BaseModel):
    teamStats: list[TeamStat]
    teamStatsGoals: list[TeamStatGoals]
