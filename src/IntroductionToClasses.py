class Team:
    def __init__(self, Name="No name", Origin="No origin"):
        self.TeamName = Name
        self.TeamOrigin = Origin

    def DefineTeamName(self, Name):
        self.TeamName = Name

    def DefineTeamOrigin(self, Origin):
        self.TeamOrigin = Origin


class Player(Team):
    def __init__(self, PlayerName, PlayerPoints, TeamName, TeamOrigin):
        Team.__init__(self, TeamName, TeamOrigin)
        self.PlayerName = PlayerName
        self.PlayerPoints = PlayerPoints

    def ScoredPoint(self):
        self.PlayerPoints += 1

    def setName(self, Name):
        self.PlayerName = Name

    def __str__(self):
        return (
            self.PlayerName
            + " Player has scored: "
            + str(self.PlayerPoints)
            + " Points"
        )


Player1 = Player("Sid", 0, "Sharks", "Chicago")

print(Player1.PlayerName)
print(Player1.PlayerPoints)

print(Player1.TeamName)
print(Player1.TeamOrigin)

Player1.ScoredPoint()
print(Player1.PlayerPoints)

Player1.setName("Lee")
print(Player1.PlayerName)

print(Player1)