# game_executer.py
from game_logic import setup_teams, conduct_battle
from utils import get_team_names
from mail_template import create_battle_report_email
from mail_sender import send_email

recipient_email = input("Please enter your email address: ")

team1, team2, team1_alignment, team2_alignment = setup_teams()

team1_complete = team1.copy()
team2_complete = team2.copy()

print("Team 1 composed by:", get_team_names(team1))
print("Team 2 composed by:", get_team_names(team2))

winner, battle_history = conduct_battle(team1, team2)

for line in battle_history:
    print(line)

print("The winning team is:", winner)

mail_text = create_battle_report_email(winner, battle_history, "Team 1", get_team_names(team1_complete), team1_alignment, "Team 2", get_team_names(team2_complete), team2_alignment)

sender_email = 'bruno.rodriguez.sep@gmail.com'
if recipient_email == '':
    recipient_email = 'brunors1204@gmail.com'
subject = 'Results from the battle!'

send_email(sender_email, recipient_email, subject, mail_text)
