class Scheduling:

    def schedule(self, phase):
        cost = 0
        locations = phase.tournament.numberOfLocations
        self.initialSchedule(phase, locations)
        return phase # TODO implement

    def initialSchedule(self, phase, locations):
        slot = 1
        for match in phase.matches:
            for pitch in range(1, (locations + 1)):
                match.setLocationTime(pitch, slot)
            slot += 1