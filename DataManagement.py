import IO
import Tournament as TN


class DataManagement:

    def __init__(self):
        self.tournament = None
        self.io = IO.IO()

    def listStoredTournaments(self):
        """
        :return: A list of strings/names of all tournaments stored on the disk.
        """
        return self.io.listAllTournaments()

    def storeTournament(self, tournament):
        """
        Store a tournament to the disk as file.
        :param tournament: the tournament to be stored.
        """
        self.io.storeTournament(tournament)

    def loadTournament(self, name):
        """
        Load a tournament from the disk and replace the current tournament with it. Make sure to store the old
            tournament before calling this function.
        :param name: of the tournament to be loaded, without file extensions.
        """
        self.tournament = self.io.loadTournament(name)

    def getTournament(self):
        """
        :return: the currently opened tournament.
        """
        return self.tournament

    def createTournament(self, identifier):
        """
        Creates a tournament and replaces the current touranment with it. Make sure to store the old tournament before
            calling this function.
        :param identifier: The name of the tournament, this will also become its file name.
        """
        self.tournament = TN.Tournament(identifier)
