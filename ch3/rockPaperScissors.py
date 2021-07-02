from random import randint, choice

#print(f'random value from 0 to 2 is : {randint(0, 2)}')
# random_choice = randint(0, 2)
#
# if random_choice == 0:
#     computer_choice = 'rock'
# elif random_choice == 1:
#     computer_choice = 'paper'
# else:
#     computer_choice = 'scissors'

#print('Computer choice is ',computer_choice)

choices = ['rock', 'paper', 'scissors']
random_choice = choice(choices)

user_choice = input('rock, paper, scissors? ').lower()
print('You choose', user_choice, 'and the computer choose', random_choice)
