
from random import choice
from time import sleep
class Hangman:
    """
     Hangman play.
    """
    _HANGMAN = (
        """
         ------
         |    |
         |
         |
         |
         |
         |
         |
         |
        ----------
        """,
        """
         ------
         |    |
         |    O
         |
         |
         |
         |
         |
         |
        ----------
        """,
        """
         ------
         |    |
         |    O
         |   -+-
         | 
         |   
         |   
         |   
         |   
        ----------
        """,
        """
         ------
         |    |
         |    O
         |  /-+-
         |   
         |   
         |   
         |   
         |   
        ----------
        """,
        """
         ------
         |    |
         |    O
         |  /-+-/
         |   
         |   
         |   
         |   
         |   
        ----------
        """,
        """
         ------
         |    |
         |    O
         |  /-+-/
         |    |
         |   
         |   
         |   
         |   
        ----------
        """,
        """
         ------
         |    |
         |    O
         |  /-+-/
         |    |
         |    |
         |   | 
         |   | 
         |   
        ----------
        """,
        """
         ------
         |    |
         |    O
         |  /-+-/
         |    |
         |    |
         |   | |
         |   | |
         |  
        ----------
        """)

    _WORDS = ("APPLE", "mirror", "ball", "TESLA","book")
    _POSITIVE_SAYINGS = ("Well done!", "Awesome!",)

    def __init__(self):

        self._word = choice(self._WORDS)
        self._so_far = "-" * len(self._word)
        self._used = []
        self._wrong_answers = 0

    def play(self):
        
        self._reset_game()
        self._start_game()


        while self._wrong_answers < len(self._HANGMAN) and self._so_far != self._word:
            self._print_current_progress()
            guess = self._user_guess()
            self._check_answer(guess)

        self._print_result()
        self._play_again()

    # ---------------------------------


    def _check_answer(self, guess):

        if guess in self._word:
            print(choice(self._POSITIVE_SAYINGS), "...Updating word so far...")

            for i in range(len(self._word)):
                if guess == self._word[i]:

                    self._so_far = self._so_far[:i] + guess + self._so_far[i+1:]

        else:
            print("INCORRECT! Try again!")
            self._wrong_answers += 1

    def _play_again(self):

        print("Would you like to play again?")
        user_input = input("Enter Y for yes or N for no: ").upper()

        if user_input == "Y":
            self.play()

        else:
            print()
            print("Thank you for playing!")

    def _print_current_progress(self):

        print()
        print(self._HANGMAN[self._wrong_answers])
        print("Word so far: ", self._so_far)
        print("Letters used: ", sorted(self._used))

    def _print_result(self):

        sleep(1)
        print()
        print("Calculating result...")
        sleep(1)
        print()
        if self._wrong_answers == len(self._HANGMAN):
            print("UNLUCKY! Better luck next time!")
        else:
            print("WINNER! Congratulations!")

    def _reset_game(self):

        self.__init__()

    def _start_game(self):

        print()
        print("\t\tWelcome to Hangman!")
        print()
        input("Press Enter to START:")

    def _user_guess(self):

        guess = input("Guess a letter: ").upper()
        sleep(1)  
        print()

        while guess in self._used:
            print("Try again... You've already used this letter")
            guess = input("Guess a letter: ").upper()
            sleep(1)
            print()

        self._used.append(guess)

        return guess

if __name__ == '__main__':
    game = Hangman()

    game.play()
