class Official:

    def __init__(self, name, positionSkills, playing = True, team = None):
        self.name = name
        self.positionSkills = positionSkills
        self.playing = playing
        self.team = team

    def getName(self):
        return self.name

    def getTeam(self):
        return self.team

    def getPositionSkills(self):
        return self.positionSkills

    def isPlaying(self):
        return self.playing