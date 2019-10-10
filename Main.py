import DataManagement as DM
import IO
import Tournament as TN
import Official as Off
import Match
import Team
import TournamentPhase as Phase


class Main:

    data = DM.DataManagement()
    data.createTournament(123)
    print(data.tournament)
    tournament = TN.Tournament(1)
    official = Off.Official("Max Mustermann", [1, 2, 3])
    print(type(official.team))
    match = Match.Match(Team.Team("Flying Foxes", tournament), Team.Team("Mighty Ducks", tournament))
    # match.setResult(120,80)
    print(match.getResult())

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
    match2.setResult((150, 100))
    print(example.getCurrentPhase().getMatches()[0].getResult())
    data.storeTournament(example)

    data.loadTournament("Example tournament")
    tn = data.getTournament()
    print("Serialized")
    print(tn.getIdentifier())
    print(tn.getCurrentPhase())
    print(example.getCurrentPhase())
    print(data.listStoredTournaments())