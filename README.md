# Pelea de Personajes (Character Fight)

## What This Game Is About
"Pelea de Personajes" (Character Fight) is a fun game where you can make superheroes and villains fight. It uses information from the [Superhero API](https://www.superheroapi.com/) to make these battles.

## Before You Start

You need a few things ready:
- Python installed on your computer.
- A computer with Windows, Linux, or macOS.

## How to Start the Game

Here’s how to set it up:

### For Linux and macOS:
```bash
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
```

### For Windows:
```bash
python -m venv env
.\env\Scripts\activate
pip install -r requirements.txt
```

### To Play the Game
Run this command:
```bash
python game_executer.py
```

## How to Play
- **Making Teams**: You make two teams with five characters in each. These characters are chosen randomly and are all different.
- **Energy Levels**: Every character gets an "Actual Stamina" number.
- **Good or Bad Teams**: A team is either good or bad, depending on what most characters are. This affects how the characters do in the game.

## The Rules
- **How Fights Work**: The game uses the Superhero API to decide how the characters fight.
- **Who Attacks First**: Characters who are faster get to attack first.
- **Figuring Out Health**: We use special formulas to figure out how much health each character has.
- **Winning the Game**: The team that has characters still standing at the end wins.

## What We Assume
- We assume that every character have at least one attack with a positive value.
