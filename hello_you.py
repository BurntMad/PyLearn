# Project 2 - Hello You! - BurntMad 28. Feb
# Learn how to gather user input, make and combine data to make meaningul outputs
# A program that can take the user input, process and output

# Collecting Data
# Ask usr for name
name = input("What is your name?: ")
# print(name)
# Ask usr for age
age = input("What is your age?: ")

# Ask usr for city
city = input("What city do you live in?: ")

# Ask usr for what they enjoy
enjoy = input("What do you enjoy the most?: ")

# Create output text
string = "Your name is {} and you are {} years old. You live in {} and enjoy {}"
output = string.format(name,age,city,enjoy)
# Print output to screen
print(output)
