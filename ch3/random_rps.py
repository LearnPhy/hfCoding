import random

random_choice = ['rock', 'paper', 'scissors']
computer_choice = random.choice(random_choice)

user_choice = input('\nChoose rock, paper or scissors!').lower()

print('You choose', user_choice, 'while computer choose', computer_choice)