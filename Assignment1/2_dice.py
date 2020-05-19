'''The dice rolling simulator will imitate the experience of rolling a dice. It will generate a random number and the user can play again and again to get a number from the dice until the user decides to quit the program.'''

import random

while True:
	dice_input = input('Enter your choice : \n1. Roll\n2. Quit\n')
	if dice_input == '1':
		print('Number on the dice is : ', random.randint(1, 6))
		print('\n')
	elif dice_input == '2':
		break
	else:
		print('Incorrect input!\n')
		continue
