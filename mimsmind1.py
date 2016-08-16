import random
import sys

def guess_game(length):

	num = str(random.randint(0, (10**int(length))-1))
	max_rounds = (2**int(length))+ int(length)

	print("\nLet's play the mimsmind1 game. You have {} guesses.".format(max_rounds))
	print("\nGuess a {}-digit number: ".format(length), end='')
	tries = 0
	while tries < max_rounds:
		try:
			user_guess = input()
			assert(len(user_guess) == int(length) and int(user_guess))
			print()
		except:
			print("\nInvalid Input. try again: ", end='')
			tries += 1
			continue
		if(user_guess == num):
			tries += 1
			print("Congratulations. You guessed the correct number in {} tries\n".format(tries))
			return
		else:
			tries += 1
			bulls = 0
			cows = 0
			for n in range(0, int(length)-1):
				if(user_guess[n] == num[n]):
					bulls += 1
				elif(user_guess[n] in num):
					cows += 1
			print("{} bull(s), {} cow(s). Try again: ".format(bulls, cows), end='')
	print('\n\nSorry. You did not guess the number in {} tries. The correct number is {}'.format(max_rounds,num))
	return




def main():
	if len(sys.argv) == 1:
		guess_game('3')
	else:
		guess_game(sys.argv[1])

if __name__ == '__main__':
	main()