import random
#list of fruits
word_list = ['apple','banana','cherry','pear','orange']
print(word_list)
#picks random words from the word list
word = random.choice(word_list)
#print randomly selected word
print(f'The random word list: {word}')
#gets user input and assign it to guess
guess = input("Enter a single letter:")
#checks if the user gives a valid input 
if len(guess) == 1 and guess.isalpha():
    print("Good Guess")
else: 
    print("Oops!This is not a valid input")