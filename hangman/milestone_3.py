import random
word_list = ['apple','banana','cherry','pear','orange']
print(word_list)
word = random.choice(word_list)
print(f'The random word list: {word}')
def check_guess(guess):
    guess.lower
    if guess in word:
        print(f"Good Guess! {guess}  is in the word")
         
    else:
        print(f"Sorry, {guess} is not in the word. Try again")


def ask_for_input():
    while True:
        guess = input("Enter a single letter:")
        if len(guess) == 1 and guess.isalpha():
           break  
        else: 
            print("Invalid letter. Please, enter a single alphabetical character.")
    check_guess(guess)
ask_for_input()