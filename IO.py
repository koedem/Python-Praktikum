import pickle


class IO:

    def __init__(self, dataManagement):
        self.dataManagement = dataManagement
        self.path = 'tournaments.ser'

    def writeToFile(self, tournament):
        binaryFile = open(tournament.getIdentifier() + self.path, mode='wb')
        pickle.dump(tournament, binaryFile)
        binaryFile.close()

    def loadFromFile(self, path):
        binaryFile = open(path + self.path, mode='rb')
        tournaments = pickle.load(binaryFile)
        binaryFile.close()
        return tournaments
