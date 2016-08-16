import random
import sys

def guess_game(length):

	num = random.randint(10**(int(length)-1), (10**int(length))-1)
	print("\nLet's play the mimsmind0 game.")
	print("\nGuess a {}-digit number: ".format(length), end='')
	tries = 0
	while True:
		try:
			user_guess = int(input())
			print()
		except:
			print("Not a number, try again: ", end='')
			tries += 1
			continue
		if(user_guess == num):
			tries += 1
			print("Congratulations. You guessed the correct number in {} tries\n".format(tries))
			break
		elif(user_guess < num):
			tries += 1
			print("Try again. Guess a higher number: ", end='')
		elif(user_guess > num):
			tries += 1
			print("Try again. Guess a lower number: ", end='')



def main():
	if len(sys.argv) == 1:
		guess_game(1)
	else:
		guess_game(sys.argv[1])

if __name__ == '__main__':
	main()
