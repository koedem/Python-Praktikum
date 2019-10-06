class Algorithms:

    def __init__(self, matchMaking, scheduling):
        self.matchMaking = matchMaking
        self.scheduling = scheduling

    def schedule(self, phase): # TODO should probably have a parameter, which MM system to use
        phase = self.matchMaking.makeMatches(phase)
        return self.scheduling.schedule(phase)