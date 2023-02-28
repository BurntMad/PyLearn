# Udemy Potion Project - BurntMad 27.Feb 2023
import random
# base health
health = 50
# 1 (Easy Mode) / 2 (Medium) / 3 (Hard)
game_difficulty = 1
# in the random function, get a random number between 25 - 50, divide by difficulty and only calc integers
potion_health = int(random.randint(25,50) / game_difficulty)
# assign base health
health = health +  potion_health

print("Player's health: ",health)
