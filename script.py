from scraper.stats import Stats
from config.database import player_stats_collection, team_stats_collection, teams_stats_goals_collection

stat = Stats()

# Team Stats
teamStats = stat.get_top_ten_teams()
# Step1: Remove existing documents
team_stats_collection.delete_many({})
# Step2: Add new teamStats
team_stats_collection.insert_many([dict(teamStat) for teamStat in teamStats])

# Teams stats based on goals
teamStatsGoals = stat.get_top_ten_teams_to_score()
# Step1: Remove existing documents
teams_stats_goals_collection.delete_many({})
# Step2: Add new teamStats
teams_stats_goals_collection.insert_many(
    [dict(teamStat) for teamStat in teamStatsGoals])


# Player Stats
playerStats = stat.get_top_ten_players()
# Step1: Remove existing documents
player_stats_collection.delete_many({})
# Step2: Add new playerStats
player_stats_collection.insert_many(
    [dict(teamStat) for teamStat in playerStats])
