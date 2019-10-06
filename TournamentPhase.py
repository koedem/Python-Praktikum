class TournamentPhase:

    def __init__(self, tournament, pairingType, numberOfRounds = 1):
        self.tournament = tournament
        self.pairingType = pairingType
        self.numberOfRounds = int(numberOfRounds)
        self.matches = []

    def getMatches(self):
        return self.matches

    def schedule(self):
        pass # TODO do we want the schedule method here? Maybe should be in DM instead, as method there calling Algorithm.schedule(phase)

    def addMatch(self, match): # Custom scheduling by simply adding matches manually
        self.matches.append(match)