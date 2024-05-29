import random
#import random module t
#list of words
word_list = ['apple','banana','cherry','pear','orange']
print(word_list)
#random choice of words are chosen 
word = random.choice(word_list)
print(f'The random word list: {word}')

def check_guess(guess):
    #checks if the given user input is in the selected random word if not print meassage for the user 
    #convert the given input to lowercase
    guess.lower
    if guess in word:
        print(f"Good Guess! {guess}  is in the word")
         
    else:
        print(f"Sorry, {guess} is not in the word. Try again")


def ask_for_input():
    #as for the user input to guess the char and checks if the user sends the valid input and prints message
    while True:
        guess = input("Enter a single letter:")
        #checks if the given user input length is equal to 1 and single alphabetical character 
        if len(guess) == 1 and guess.isalpha():
           break  
        else: 
            print("Invalid letter. Please, enter a single alphabetical character.")
    check_guess(guess) #calling check_guess method
ask_for_input() #calling ask_for_input method