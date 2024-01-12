# Pelea de Personajes

## Overview
"Pelea de personajes" is a game that simulates battles between superheroes and villains using the [Superhero API](https://www.superheroapi.com/). 

## Prerequisites

Before you begin, ensure you have met the following requirements:
- You have installed the latest version of Python
- You have a `<Windows/Linux/Mac>` machine. 

## Run the challenge script

Follow these steps:

Linux and macOS:
```
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
```

Windows:
```
python -m venv env
.\env\Scripts\activate
pip install -r requirements.txt
```

Then:

```
python game_executer.py
```

## Gameplay
- **Team Formation**: Each player creates two teams of five characters each, chosen randomly without repetition.
- **Stamina Assignment**: Each character is assigned an "Actual Stamina" value.
- **Team Alignment**: A team is classified as good or evil based on the majority of its members. Characters receive bonuses or penalties based on their alignment relative to their team's.

## Rules
- **Battle Simulation**: Battles are simulated using characters' stats from the Superhero API.
- **Fight Order**: In each turn, the characters attacks a random adversary from the opposing team, the fastest characters go first.
- **Health Points Calculation**: Health points are calculated based on specific formulas.
- **Determining the Winner**: The winning team is the one with the last standing character(s).


## Optional Challenge
- **Email Integration**: Integrate an email API to send summaries of the battles.


