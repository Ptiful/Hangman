import random
from typing import List, Union


class Hangman:
    """Hangman is a game that allows you to find an hidden word, with a certain amount of guesses.
    You need to find the word before your lives are exhausted."""

    def __init__(self):
        """Self.lives would be your amount of lives before the game stops.
        SelF.error_count would be your error count, each time you are wrong it will decrease your life by 1.
        self.turn_count count the turn you spent to find the word or looses.
        self.wrongly_guessed_letters is list that will contains all your errors.
        self.possible_words is the list that will contains all words to be found.
        self.word_to_find is picking a random word in self.possible_words
        self.correctly_guesses_letters is the words in underscore,
        the underscore will be replaced by the right letter once it will be discovered.
        """
        self.lives = 5
        self.error_count = 0
        self.turn_count = 0
        self.wrongly_guessed_letters = []
        self.possible_words = ["becode", "learning", "mathematics", "sessions"]
        self.word_to_find = list(random.choice(self.possible_words))
        self.correctly_guessed_letters = ["_"] * len(self.word_to_find)
        print(f"The word to find is {self.correctly_guessed_letters}")

    def play(self):
        """Defines game restrictions, append to a list the right/wrong guessed letters,
        count lives, turns and errors, print everything at the end of a turn
        """
        while self.correctly_guessed_letters != self.word_to_find and self.lives != 0:
            player_input = input("Please chose a letter and only one letter : ")
            if player_input.isdigit():
                print("Only letter, as I told you, once more and you'll be evicted")
            elif len(player_input) >= 2:
                print("Don't mess with me, I am an angre program, one letter please")
            elif player_input in self.word_to_find:
                for i in range(len(self.word_to_find)):
                    if self.word_to_find[i] == player_input:
                        self.correctly_guessed_letters[i] = player_input
            else:
                self.wrongly_guessed_letters.append(player_input)
                self.error_count += 1
                self.lives -= 1
            self.turn_count += 1
            print(
                f"correctly_guessed_letters : {self.correctly_guessed_letters},\n bad_guessed_letters : {self.wrongly_guessed_letters},\n life: {self.lives},\n error_count:{self.error_count},\n turn count:{self.turn_count}"
            )

    def game_over(self):
        """if lives goes to 0, print "game over" and ends the game."""
        print("game over...")

    def well_played(self):
        """if the guessed word is found, print the word, the turn count, and the errors count"""
        if self.correctly_guessed_letters == self.word_to_find:
            print(
                f"You found the word : {self.word_to_find} in {self.turn_count} turns with {self.error_count} errors !"
            )

    def start_game(self):
        """Start the all game calling the play, game_over and or well_play definition from the Hangman Class"""
        self.play()
        self.game_over()
        self.well_played()


player1 = Hangman()
player1.start_game()
