class Team:
    def __init__(self):
        self.TeamName = "NaN"
        self.TeamOrigin = "NaN"

    def DefineTeamName(self, Name):
        self.TeamName = Name

    def DefineTeamOrigin(self, Origin):
        self.TeamOrigin = Origin


Team1 = Team()

print(Team1.TeamName)

Team1.DefineTeamName("Tigers")
Team1.DefineTeamOrigin("Chicago")
print(Team1.TeamName)
print(Team1.TeamOrigin)