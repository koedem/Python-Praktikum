class Match:

    def __init__(self, teamOne, teamTwo, priority = 0, score=(0,0), location = None, time = None):
        self.teamOne = teamOne
        self.teamTwo = teamTwo
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