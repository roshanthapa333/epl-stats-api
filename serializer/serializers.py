from fastapi.encoders import jsonable_encoder

from models.stats import TeamStat, PlayerStat, TeamStatGoals


def serialize_team_stat(teamStat) -> dict:
    return {"id": str(teamStat["_id"]), **jsonable_encoder(TeamStat(**teamStat))}


def serialize_team_stats(teamStats) -> list:
    return [serialize_team_stat(teamStat) for teamStat in teamStats]


def serialize_team_stat_goals(teamsStatGoals) -> dict:
    return {"id": str(teamsStatGoals["_id"]), **jsonable_encoder(TeamStatGoals(**teamsStatGoals))}


def serialize_team_stats_goals(teamsStatsGoals) -> list:
    return [serialize_team_stat_goals(teamsStatGoal) for teamsStatGoal in teamsStatsGoals]


def serialize_player_stat(playerStat) -> dict:
    return {"id": str(playerStat["_id"]), **jsonable_encoder(PlayerStat(**playerStat))}


def serialize_player_stats(playerStats) -> list:
    return [serialize_player_stat(playerStat) for playerStat in playerStats]
