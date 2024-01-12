def create_battle_report_email(winning_team, battle_attacks, team1_name, team1_members, team1_alignment, team2_name, team2_members, team2_alignment):
    # Define the email template in HTML with inline CSS styles and responsive design
    email_template = f"""
    <html>
    <head>
        <style>
            body {{
                font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
                margin: 0;
                padding: 0;
                background-color: #f7f7f7;
                color: #555;
                -webkit-text-size-adjust: 100%;
                -ms-text-size-adjust: 100%;
            }}
            .container {{
                max-width: 650px;
                margin: 20px auto;
                padding: 20px;
                background-color: #fff;
                box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
                border-radius: 8px;
            }}
            h1 {{
                color: #333;
                text-align: center;
                font-size: 30px;
                margin-bottom: 20px;
            }}
            h2 {{
                color: #333;
                font-size: 24px;
                border-bottom: 1px solid #ddd;
                padding-bottom: 5px;
            }}
            h3 {{
                font-size: 20px;
                color: #333;
            }}
            p, li {{
                font-size: 16px;
                line-height: 1.6;
                color: #555;
            }}
            ul {{
                list-style-type: none;
                padding-left: 20px;
            }}
            li {{
                margin-bottom: 10px;
                position: relative;
            }}
            li:before {{
                content: '';
                width: 6px;
                height: 6px;
                background-color: #88c057;
                border-radius: 50%;
                position: absolute;
                left: -14px;
                top: 10px;
            }}
            .team-member {{
                font-weight: bold;
            }}
            .alignment-good {{
                color: #6495ED;
            }}
            .alignment-bad {{
                color: #DC143C;
            }}
            .footer {{
                text-align: center;
                margin-top: 40px;
                font-size: 14px;
                color: #999;
                border-top: 1px solid #ddd;
                padding-top: 15px;
            }}
            @media only screen and (max-width: 600px) {{
                .container {{
                    width: 100%;
                    margin: 10px auto;
                    padding: 10px;
                }}
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Battle Report: Victory Announcement</h1>
            <p>The momentous battle has concluded with <b>{winning_team}</b> triumphing gloriously!</p>
            
            <h2>Team Overviews:</h2>
            <div>
                <h3>{team1_name} - The Gallant Warriors</h3>
                <ul>
                    {format_team_members(team1_members, team1_alignment)}
                </ul>
            </div>
            <div>
                <h3>{team2_name} - The Formidable Challengers</h3>
                <ul>
                    {format_team_members(team2_members, team2_alignment)}
                </ul>
            </div>
            
            <h2>Key Battle Highlights:</h2>
            <ul>
                {format_battle_attacks(battle_attacks)}
            </ul>
            <p class="footer">A hearty congratulations to <b>{winning_team}</b> for their strategic mastery and valor!<br>Best regards,<br>Bruno</p>
        </div>
    </body>
    </html>
    """

    return email_template

def format_battle_attacks(attacks):
    return "\n".join([f"<li>{attack}</li>" for attack in attacks])

def format_team_members(members, alignment):
    alignment_class = f'alignment-{alignment}'
    return "\n".join([f"<li class='team-member {alignment_class}'>{member}</li>" for member in members])

if __name__ == '__main__':
    winning_team = "Heroes"
    battle_attacks = ["Power Strike", "Magic Blast", "Shield Defense"]
    team1_name = "The Guardians"
    team1_members = ["Hero1", "Hero2", "Hero3"]
    team2_name = "The Invaders"
    team2_members = ["Villain1", "Villain2", "Villain3"]
    team1_alignment = "good"
    team2_alignment = "bad"

    email_content = create_battle_report_email(winning_team, battle_attacks, team1_name, team1_members, team1_alignment, team2_name, team2_members, team2_alignment)

    # Print or send the HTML email content as needed
    print(email_content)
