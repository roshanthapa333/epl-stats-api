import requests
from bs4 import BeautifulSoup
from models.stats import TeamStat, PlayerStat, TeamStatGoals


class Stats():
    """
        Gets the statistics of teams and players
    """
    URL = "https://www.premierleague.com"

    def get_top_ten_teams(self):
        """
            Gets the top teams with match played and points earned
        """
        page = requests.get(self.URL+"/tables")
        soup = BeautifulSoup(page.content, 'html.parser')
        table = soup.find("tbody", class_="league-table__tbody")
        tableRows = table.find_all(
            "tr", {'data-filtered-table-row-name': True})

        data: list[TeamStat] = []

        for row in tableRows[:10]:
            teamName = row.find(
                "span", class_="league-table__team-name").get_text().strip()
            points = row.find(
                "td", class_="league-table__points").get_text().strip()
            matchPlayed = row.find_all("td")[2].get_text().strip()
            data.append(TeamStat(teamName=teamName,
                        matchPlayed=matchPlayed, points=points))

        return data

    def get_top_ten_teams_to_score(self):
        """
            Gets the top 10 teams based on goals scored
        """
        page = requests.get(self.URL+"/stats/top/clubs/goals")
        soup = BeautifulSoup(page.content, 'html.parser')
        table = soup.find("tbody", class_="statsTableContainer")
        tableRows = table.find_all("tr")

        data: list[TeamStatGoals] = []

        for row in tableRows[:10]:
            teamName = row.find(
                "td", class_="stats-table__name").get_text().strip()
            goals = row.find_all("td")[2].get_text().strip()
            data.append(TeamStatGoals(teamName=teamName, goals=goals))

        return data

    def get_top_ten_players(self):
        """
            Gets the top 10 players based on goals scored
        """
        page = requests.get(self.URL+"/stats/top/players/goals")
        soup = BeautifulSoup(page.content, 'html.parser')
        table = soup.find("tbody", class_="stats-table__container")
        tableRows = table.find_all("tr")

        data: list[PlayerStat] = []
        for row in tableRows[:10]:
            playerName = row.find(
                "td", class_="stats-table__name").get_text().strip()
            teamName = row.find_all("td")[2].get_text().strip()
            goals = row.find(
                "td", class_="stats-table__main-stat").get_text().strip()
            data.append(PlayerStat(playerName=playerName,
                        teamName=teamName, goals=goals))

        return data
