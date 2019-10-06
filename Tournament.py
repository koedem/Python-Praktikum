import TournamentPhase as Phase

class Tournament:

    def __init__(self, identifier, numberOfLocations = 1, officialPositions = None):
        self.identifier = identifier
        self.numberOfLocations = numberOfLocations
        self.officialPositions = officialPositions
        self.teams = []
        self.officials = []
        self.phases = []

    def addTeam(self, team):
        self.teams.append(team)

    def addOfficial(self, official):
        self.officials.append(official)

    def getIdentifier(self):
        return self.identifier

    def addPhase(self, pairingType, numOfRounds):
        self.phases.append(Phase.TournamentPhase(self, pairingType, numberOfRounds=numOfRounds))

    def getCurrentPhase(self):
        return self.phases[-1]