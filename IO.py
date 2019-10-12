import pickle
import glob


class IO:

    def __init__(self):
        self.fileExtension = '.tour'

    def listAllTournaments(self):
        return glob.glob("./*" + self.fileExtension)

    def storeTournament(self, tournament):
        binaryFile = open(tournament.getIdentifier() + self.fileExtension, mode='wb')
        pickle.dump(tournament, binaryFile)
        binaryFile.close()

    def loadTournament(self, name):
        binaryFile = open(name + self.fileExtension, mode='rb')
        tournament = pickle.load(binaryFile)
        binaryFile.close()
        return tournament
