class Team:

    def __init__(self, name, tournament, rating = 0):
        self.name = name
        self.tournament = tournament
        self.rating = rating

    def getName(self):
        return self.name