class Match:

    def __init__(self, teamOne, teamTwo, officialPositions, priority = 0, score=(0,0), location = None, time = None):
        self.teamOne = teamOne
        self.teamTwo = teamTwo
        self.officials = [(pos, "") for pos in officialPositions]
        self.priority = priority
        self.score = score
        self.locTime = (location, time) # initialize with None in case locTime gets requested before the match got scheduled

    def setLocationTime(self, location, time):
        self.locTime = (location, time)

    def getLocationTime(self, location, time):
        return self.locTime


    def setResult(self, score):
        """
        :param score: tuple containing the score of team one and team two, example: (150,100)
        """
        self.score = score

    def getResult(self):
        """
        :return: tuple containing the score of team one and team two, example: (150,100)
        """
        return self.score

    def getTeams(self):
        return (self.teamOne, self.teamTwo)

    def print(self):
        print(self.teamOne.getName() + " (" + str(self.score[0]) + ") vs (" + str(self.score[1]) + ") "
              + self.teamTwo.getName() + ". Pitch: " + str(self.locTime[0]) + ", slot: " + str(self.locTime[1]))
