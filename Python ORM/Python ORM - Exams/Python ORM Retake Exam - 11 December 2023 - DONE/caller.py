import os
import django

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models here
from main_app.models import Tournament, TennisPlayer, Match
from django.db.models import F, Q, Avg, Count


def get_tennis_players(search_name=None, search_country=None):
    if search_name is None and search_country is None:
        return ""

    query = Q()
    query_names = Q(full_name__icontains=search_name)
    query_countries = Q(country__icontains=search_country)

    if search_name and search_country:
        query |= query_names & query_countries
    elif search_name:
        query |= query_names
    else:
        query |= query_countries

    players = TennisPlayer.objects.filter(query).order_by('ranking')

    if not players:
        return ""

    result = []
    [result.append(f"Tennis Player: {p.full_name}, country: {p.country}, ranking: {p.ranking}") for p in players]

    return "\n".join(result)


def get_top_tennis_player():
    player = TennisPlayer.objects.get_tennis_players_by_wins_count().first()
    if not player:
        return ""
    return f"Top Tennis Player: {player.full_name} with {player.num_wins} wins."


def get_tennis_player_by_matches_count():
    player = TennisPlayer.objects.annotate(num_matches=Count('matches')).order_by('-num_matches', 'ranking').first()
    if not player or player.num_matches == 0:
        return ""
    return f"Tennis Player: {player.full_name} with {player.num_matches} matches played."


def get_tournaments_by_surface_type(surface=None):
    if surface is None:
        return ""

    matching_tournaments = Tournament.objects.prefetch_related('matches').annotate(num_matches=Count('matches')).filter(surface_type__icontains=surface).order_by('-start_date')

    result = []
    [result.append(f"Tournament: {t.name}, start date: {t.start_date}, matches: {t.num_matches}") for t in matching_tournaments]

    return "\n".join(result) if result else ''


def get_latest_match_info():
    last_match = Match.objects.prefetch_related('players').order_by('-date_played', '-id').first()
    if not last_match:
        return ''

    player_names = ' vs '.join(player.full_name for player in last_match.players.all().order_by('full_name'))
    tournament_name = last_match.tournament.name
    return f"Latest match played on: {last_match.date_played}, tournament: {tournament_name}, score: {last_match.score}, players: {player_names}, winner: {'TBA' if last_match.winner is None else last_match.winner.full_name}, summary: {last_match.summary}"


def get_matches_by_tournament(tournament_name=None):
    if tournament_name is None:
        return "No matches found."

    matches = Match.objects.select_related('tournament', 'winner').filter(tournament__name__exact=tournament_name).order_by('-date_played')

    if not matches:
        return "No matches found."

    result = []
    [result.append(f"Match played on: {m.date_played}, score: {m.score}, winner: {m.winner.full_name if m.winner else 'TBA'}") for m in matches]

    return "\n".join(result)


