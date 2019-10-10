import IO
import Tournament as TN


class DataManagement:

    def __init__(self):
        self.tournaments = {}
        self.io = IO.IO()

    def listStoredTournaments(self):
        return self.io.listAllTournaments()

    def storeTournament(self, tournament):
        self.io.storeTournament(tournament)

    def loadTournament(self, name):
        return self.io.loadTournament(name)

    def getTournament(self, identifier):
        return self.tournaments[identifier]

    def addTournament(self, identifier):
        self.tournaments[identifier] = TN.Tournament(identifier)

    def getAllTournaments(self):
        return iter(self.tournaments.values())
