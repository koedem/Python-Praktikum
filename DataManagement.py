import Tournament as TN

class DataManagement:

    def __init__(self):
        self.tournaments = {}

    def getTournament(self, identifier):
        return self.tournaments[identifier]

    def addTournament(self, identifier):
        self.tournaments[identifier] = TN.Tournament(identifier)

    def getAllTournaments(self):
        return iter(self.tournaments.values())