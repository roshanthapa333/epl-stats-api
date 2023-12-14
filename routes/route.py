from fastapi import APIRouter
from bson import ObjectId

from config.database import team_stats_collection, player_stats_collection, teams_stats_goals_collection
from serializer.serializers import serialize_team_stats, serialize_player_stats, serialize_team_stats_goals
from models.stats import PlayerStat, TeamStatsResponseModal


router = APIRouter()


@router.get('/',  tags=["health"])
async def check_health():
    """
        Checks api health
    """
    return "OK"


@router.get('/team-stats', response_model=TeamStatsResponseModal)
async def team_stats():
    """
        Returns teams stats
    """
    teamStatsCursor = team_stats_collection.find()
    teamStatsGoalsCursor = teams_stats_goals_collection.find()
    teamStats = serialize_team_stats(teamStatsCursor)
    teamStatsGoals = serialize_team_stats_goals(teamStatsGoalsCursor)
    return {"teamStats": teamStats, "teamStatsGoals": teamStatsGoals}


@router.get('/player-stats', response_model=list[PlayerStat])
async def player_stats():
    """
        Returns player stats
    """
    playerStatsCursor = player_stats_collection.find()
    playerStats = serialize_player_stats(playerStatsCursor)
    return playerStats
