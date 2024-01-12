# game_logic.py
from utils import create_team, assign_stamina, determine_team_alignment, apply_alignment_bonus, compute_team_hp, get_team_names, simulate_battle

NUM_CHARACTERS_PER_TEAM = 5

def setup_teams():
    team1 = create_team(NUM_CHARACTERS_PER_TEAM)
    team2 = create_team(NUM_CHARACTERS_PER_TEAM)
    assign_stamina(team1)
    assign_stamina(team2)
    team1_alignment = determine_team_alignment(team1)
    team2_alignment = determine_team_alignment(team2)
    apply_alignment_bonus(team1, team1_alignment)
    apply_alignment_bonus(team2, team2_alignment)
    compute_team_hp(team1 + team2)
    return team1, team2, team1_alignment, team2_alignment

def conduct_battle(team1, team2):
    return simulate_battle(team1, team2)
