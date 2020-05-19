'''Make a program that randomly chooses a number to guess and then the user will have a few chances to guess the number correctly. In each wrong attempt, the computer will give a hint that the number is greater or smaller than the one you have guessed.'''

import random

def guess_num(n) :
	while True :
		guess = int(input('Guess the number : '))
	
		if guess == n :
			print('You guessed the right number!')
			break
			
		elif guess > n:
			print('You guessed the wrong number!')
			print('Hint : The number is smaller than %d\n' %(guess))
		
		elif guess < n:
			print('You guessed the wrong number!')
			print('Hint : The number is greater than %d\n' %(guess))
		
if __name__ == '__main__' :
	ran = input('Enter the range in which you want to guess the number separated by a space :\n').split()
	s = int(ran[0])
	e = int(ran[1])

	n = random.randint(s, e)
	guess_num(n)

		
