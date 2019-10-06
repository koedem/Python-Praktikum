class Match:

    def __init__(self, teamOne, teamTwo, priority = 0, scoreTeamOne = 0, scoreTeamTwo = 0, location = None, time = None):
        self.teamOne = teamOne
        self.teamTwo = teamTwo
        self.priority = priority
        self.scoreTeamOne = scoreTeamOne # initialize with 0 in case result gets requested before the match happens
        self.scoreTeamTwo = scoreTeamTwo # TODO should this already be a tupel?
        self.locTime = (location, time) # initialize with None in case locTime gets requested before the match got scheduled

    def setLocationTime(self, location, time):
        self.locTime = (location, time)

    def getLocationTime(self, location, time):
        return self.locTime

    def setResult(self, scoreTeamOne, scoreTeamTwo):
        self.scoreTeamOne = scoreTeamOne
        self.scoreTeamTwo = scoreTeamTwo

    def getResult(self):
        return (self.scoreTeamOne,self.scoreTeamTwo)

    def getTeams(self):
        return (self.teamOne, self.teamTwo)