import math
import requests
import random
import configparser
from typing import Optional, List, Dict

# Load API Key from a configuration file
config = configparser.ConfigParser()
config.read('config.ini')
API_KEY = config.get('DEFAULT', 'API_KEY')

def get_random_character(api_url: str = "https://superheroapi.com/api") -> Optional[Dict]:
    """Fetch a random character from the API."""
    character_id = random.randint(1, 731)
    response = requests.get(f"{api_url}/{API_KEY}/{character_id}")
    
    if response.status_code == 200:
        return response.json()
    else:
        return None

def create_team(size: int) -> List[Dict]:
    """Create a team of unique characters."""
    team = []
    while len(team) < size:
        character = get_random_character()
        if character and all(character['id'] != member['id'] for member in team):
            convert_powerstats_to_double(character)
            team.append(character)
    return team

def get_team_names(team: List[Dict]) -> List[str]:
    """Get the names of the characters in a team."""
    return [character['name'] for character in team]

def convert_powerstats_to_double(character: Dict) -> None:
    """Convert powerstats from string to double."""
    for key, value in character['powerstats'].items():
        character['powerstats'][key] = float(value) if value != 'null' else 0.0

def assign_stamina(team: List[Dict]) -> None:
    """Assign a random stamina value to each character."""
    for character in team:
        character['actual_stamina'] = random.uniform(0, 10)

def determine_team_alignment(team: List[Dict]) -> str:
    """Determine the majority alignment of the team."""
    alignments = [character['biography']['alignment'] for character in team]
    return 'good' if alignments.count('good') > alignments.count('bad') else 'bad'


def apply_alignment_bonus(team: List[Dict], team_alignment: str) -> None:
    """Apply bonuses or penalties based on team alignment."""
    for character in team:
        if character['biography']['alignment'] == team_alignment:
            character['FB'] = 1 + random.randint(0, 9)
        else:
            character['FB'] = (1 + random.randint(0, 9)) ** -1

def compute_initial_hp(character: Dict) -> None:
    """Calculate the initial HP of a character."""
    strength = character['powerstats']['strength']
    durability = character['powerstats']['durability']
    power = character['powerstats']['power']
    stamina = character['actual_stamina']
    
    character['hp'] = math.floor((strength * 0.8 + durability * 0.7 + power) * 0.5 * (1 + stamina / 10.0)) + 100

def compute_team_hp(team: List[Dict]) -> None:
    """Calculate the initial HP of a team."""
    for character in team:
        compute_initial_hp(character)

def simulate_attack(attacker: Dict, defender: Dict) -> bool:
    """Simulate an attack from the attacker to the defender and update HP."""
    attack_type = random.choice(['mental', 'strong', 'fast'])
    damage = calculate_attack_damage(attacker, attack_type)
    defender['hp'] -= damage
    return defender['hp'] <= 0, f"{attacker['name']} attacks {defender['name']} with a {attack_type} attack causing {damage:.2f} damage"

def calculate_attack_damage(character: Dict, attack_type: str) -> float:
    """Calculate the damage of an attack based on type."""
    powerstats = character['powerstats']
    FB = character['FB']

    if attack_type == 'mental':
        return (powerstats['intelligence'] * 0.7 + powerstats['speed'] * 0.2 + powerstats['combat'] * 0.1) * FB
    elif attack_type == 'strong':
        return (powerstats['strength'] * 0.6 + powerstats['power'] * 0.2 + powerstats['combat'] * 0.2) * FB
    else:  # fast
        return (powerstats['speed'] * 0.55 + powerstats['durability'] * 0.25 + powerstats['strength'] * 0.2) * FB

def simulate_battle(team1: List[Dict], team2: List[Dict]) -> str:
    """Simulate a battle between two teams and determine the winner."""
    # characters should attack in order of speed
    attack_order = team1 + team2
    attack_order.sort(key=lambda character: character['powerstats']['speed'], reverse=True)

    attack_history = []

    while team1 and team2:
        for character in attack_order:
            if character['hp'] <= 0:
                continue
            if character in team1:
                team, winning = team2, 'Team 1'
            else:
                team, winning = team1, 'Team 2'
            defender = random.choice(team)
            character_won, attack_string = simulate_attack(character, defender)
            attack_history.append(attack_string)
            if character_won:
                attack_history.append(f"{defender['name']} has been defeated")
                team.remove(defender)
                if not team:
                    return winning, attack_history