import random
class Hangman:
    def __init__(self, word_list, num_lives = 5):
        self.word = random.choice(word_list)       
        self.word_guessed = ['_'  for _ in  self.word]
        self.num_letters = len(set(self.word))
        self.num_lives = num_lives
        self.word_list = word_list
        self.list_of_guesses = []

    def check_guess(self,guess):
        guess.lower
        
        if guess in self.word:
            print(f"Good Guess! {guess}  is in the word") 
            for i,letter in enumerate(self.word):
                if letter == guess:
                    self.word_guessed[i]=guess
            self.num_letters-=1
        else:
            print(f"Sorry, {guess} is not in the word.")
            self.num_lives-=1
            print(f"You have {self.num_lives} lives left.")
            
     
    def ask_for_input(self):
        while True:
            guess = input("Enter a single letter:")
            if len(guess) != 1 or not guess.isalpha():
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print(f"You already tried that letter!") 
                #break                
            else: 
                self.check_guess(guess)
                self.list_of_guesses.append(guess)
                #break
    
word_list = ['apple','banana','cherry','pear','orange']
hangman = Hangman(word_list)
hangman.ask_for_input()