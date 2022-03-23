"""
Open Source Projects - Final Project
Authors: Rhys Lynch | Kian Cliffe | Darragh Foran
Description: A python-based game engine that will create and play text-based adventure games
"""
# This main file will allow the user to choose their story from available stories.
import os.path
import time
import os
import engine

story_folder = 'Stories'
available_games = 0
games_list = []
games_showcase = []

for base, dirs, files in os.walk(story_folder):
    for file in files:
        available_games += 1
        games_list.append(file)
        file = file[:-3]
        games_showcase.append(file)

print('\nAdventures Loaded:', available_games)
print("\nWelcome! Choose a story to begin!\n")

i = 1
for game in games_showcase:
    print(str(i) + ".", game)
    i += 1

while 1:
    print()
    story_choice = input("> ")

    if story_choice.isalpha():
        print("[ERROR] input numbers only.")

    elif (int(story_choice) <= 0) or (int(story_choice) > len(games_list)):
        print("[ERROR] number not an option.")

    else:
        print(games_showcase[int(story_choice) - 1], "story is loading. Enjoy!")
        time.sleep(3)
        clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')
        clearConsole()
        exec(open(games_list[int(story_choice)]).read())
        engine.run(games_showcase[int(story_choice) - 1])

