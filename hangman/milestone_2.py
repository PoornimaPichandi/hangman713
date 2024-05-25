import random
word_list = ['apple','banana','cherry','pear','orange']
print(word_list)

word = random.choice(word_list)
print(f'The random word list: {word}')
guess = input("Enter a single letter:")
if guess.isalpha() and len(guess) == 1 :
    print("Good Guess")
else: 
    print("Oops!This is not a valid input")