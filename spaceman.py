import random

guessed_right = []
guessed_wrong =[]
awnser = []

def load_word():
	f = open('words.txt', 'r')
	words_list = f.readlines()
	f.close()

	words_list = words_list[0].split(' ')
	secret_word = random.choice(words_list)
	return secret_word


def make_list(word):
	length = len(word)
	num = 0

	while num < length:
		guessed_right.append("_")
		num += 1

	for char in word:
		awnser.append(char)

	return (guessed_right, awnser)

def update_list(guessed, guessed_right, awnser):
	reoccurring_char = awnser.count(guessed)

	check = awnser.index(guessed)
	guessed_right[check] = guessed

	if reoccurring_char > 1:
		num = 0
		while num < len(awnser):
			if awnser[num] == guessed:
				guessed_right[num] = awnser[num]
			num += 1

	return guessed_right

def draw_man(num):
	if num == 6:
		print(r"""
   |		
  /.\
 /...\
/.....\
|-----|		
|  o  |
|     |
|     |
|     |    
|-----|
  /.\
  --- """)
		
	elif num == 5:
		print(r"""
   |		
  /.\
 /...\
/.....\
|-----|		
|  o  |
|/    |
|     |
|     |    
|-----|
  /.\
  --- """)
		
	elif num == 4:
		print(r"""
   |
  /.\
 /...\
/.....\
|-----|		
|  o  |
|/ |  |
|     |
|     |    
|-----|
  /.\
  --- """)
		
	elif num == 3:
		print(r"""
   |
  /.\
 /...\
/.....\
|-----|		
|  o  |
|/ | \|
|     |
|     |    
|-----|
  /.\
  --- """)
		
	elif num == 2:
		print(r"""
   |
  /.\
 /...\
/.....\
|-----|		
|  o  |
|/ | \|
|  |  |
|     |    
|-----|
  /.\
  --- """)
		
	elif num == 1:
		print(r"""
   |
  /.\
 /...\
/.....\
|-----|		
|  o  |
|/ | \|
|  |  |
| /   |    
|-----|
  /.\
  --- """)
		
	elif num == 0:
		print(r"""
   |
  /.\
 /...\
/.....\
|-----|		
|  o  |
|/ | \|
|  |  |
| / \ |    
|-----|
  /.\
  --- """)
	else:
		pass


def space_man():
	guessed_incorrect = 7

	while guessed_incorrect != 0 and awnser != guessed_right:

		print("Secret Word: " + str(guessed_right))
		print("Incorrect Words that have been attemped: " + str(guessed_wrong))
		print("Number of incorrect attempts allowed: " + str(guessed_incorrect))

		guess = input("Choose a letter: ")

		if len(guess) != 1:
			print("One letter per guess. Try Again!")

		elif guess in awnser:
			print("The letter " + guess + " is in the secret word")
			update_list(guess, guessed_right, awnser)
		else:
			print("Letter is not in word! Try something else!")
			guessed_incorrect -= 1
			draw_man(guessed_incorrect)
			guessed_wrong.append(guess)			

	if guessed_incorrect <= 0:
		print("You just sent a man to SPACE! The word was " + secret_word +"!")
	else:
		print(guessed_right)
		print("Congrats you guessed right! You just saved a man from being lauched into SPACE!")

secret_word = load_word()
make_list(secret_word)
space_man()