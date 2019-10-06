import DataManagement as DM
import Tournament as TN
import Official as Off
import Match
import Team
import TournamentPhase as Phase

class Main:

    data = DM.DataManagement()
    data.addTournament(123)
    print(data.tournaments)
    tournament = TN.Tournament(1)
    official = Off.Official("Max Mustermann", [1, 2, 3])
    print(type(official.team))
    match = Match.Match(Team.Team("Flying Foxes", tournament), Team.Team("Mighty Ducks", tournament))
    # match.setResult(120,80)
    print(match.getResult())
    for tn in data.getAllTournaments():
        print(tn.getIdentifier())

    example = TN.Tournament("Example tournament")
    foxes = Team.Team("Flying Foxes", example, rating=2100)
    ducks = Team.Team("Mighty Ducks", example, rating=1800)
    example.addTeam(foxes)
    example.addTeam(ducks)
    example.addPhase("Swiss System", 7)
    match2 = Match.Match(foxes, ducks)
    example.getCurrentPhase().addMatch(match)
    example.getCurrentPhase().schedule()
    print(example.getCurrentPhase().getMatches()[0].getResult())
    match2.setResult(150, 100)
    print(example.getCurrentPhase().getMatches()[0].getResult()) # TODO why isn't this 150-100 ? Check immutability stuff etc
