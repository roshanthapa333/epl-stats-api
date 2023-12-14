import os
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

client = MongoClient(os.getenv("DB_URL"))

db = client.eplstats

team_stats_collection = db["team_stats"]
teams_stats_goals_collection = db["team_stats_goals"]
player_stats_collection = db["player_stats"]
