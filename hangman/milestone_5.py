import random
class Hangman:
    '''
    A Hangman Game that asks the user for a letter and checks if it is in the word.
    It starts with a default number of lives and a random word from the word_list.

    
    Parameters:
    ----------
    word_list: list
        List of words to be used in the game
    num_lives: int
        Number of lives the player has
    
    Attributes:
    ----------
    word: str
        The word to be guessed picked randomly from the word_list
    word_guessed: list
        A list of the letters of the word, with '_' for each letter not yet guessed
        For example, if the word is 'apple', the word_guessed list would be ['_', '_', '_', '_', '_']
        If the player guesses 'a', the list would be ['a', '_', '_', '_', '_']
    num_letters: int
        The number of UNIQUE letters in the word that have not been guessed yet
    num_lives: int
        The number of lives the player has
    list_of_guess: list
        A list of the letters that have already been tried

    Methods:
    -------
    check_guess(guessing letter)
        Checks if the letter is in the word.
    ask_for_input()
        Asks the user for a letter.
    '''

       
    def __init__(self, word_list, num_lives = 5):
        self.word = random.choice(word_list)       
        self.word_guessed = ['_'  for _ in  self.word]
        self.num_letters = len(set(self.word))
        self.num_lives = num_lives
        self.word_list = word_list
        self.list_of_guesses = []

 
    def check_guess(self,guess):
        '''
        Checks if the input letter is in the word If yes Print Good Guess.
        If it is, then replaces the '_' in the word_guessed list with the letter and subtracts the number of word guessed from 
        the number of words.
        If it is not, it reduces the number of lives by 1 and Print sorry the input guess is not in the word and another 
        Print says the number of lives remaining to play the game.
        '''
        guess.lower
        
        if guess in self.word:
            print(f"Good Guess! {guess}  is in the word") 
            for i,letter in enumerate(self.word):                
                if letter == guess:
                    self.word_guessed[i]=guess
            self.num_letters = len(set(self.word) - set(self.word_guessed)) 
        else:
            self.num_lives-=1
            print(f"Sorry, {guess} is not in the word.")
            print(f"You have {self.num_lives} lives left.")
            
     
    def ask_for_input(self):
        '''
        Asks the user for a letter and checks two possiblities:
        1. If the letter has already been tried
        2. If the character is a single character
        If it passes both checks, it calls the check_guess method and appends in list_of_guesses.
        '''
        while True:
            guess = input("Enter a single letter:")
            if len(guess) != 1 or not guess.isalpha():
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print(f"You already tried that letter!")                               
            else: 
                self.check_guess(guess)
                self.list_of_guesses.append(guess)
                break

def play_game(word_list):
    '''
        Iteratively ask the user for a letter calling the ask_for_input method
        until the user guesses the word or runs out of lives  
        1. If the user guesses the word correctly, print "Congratulations! You won the game!" and exit
        2. If the user runs out of lives , print "You lost!" and exit
    '''
    num_lives = 5
    game = Hangman(word_list, num_lives)
    while True:
        if game.num_lives == 0:
            print(f"You Lost.")
            break
        elif game.num_letters > 0 and num_lives!=0:
            game.ask_for_input()
        else:    
            print(f'Congratulations. You won the game!')
            break

word_list = ['Mango','Apple','cherry','kiwi','orange'] 
play_game(word_list) ##calling play_game method and passing the wordlist argument

        
