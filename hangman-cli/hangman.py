import sys
from os import system
from time import sleep

sys.path.append("..")

from rich import print
from words.wordgen import *  # NOQA


def welcome_screen():
    for word in ["[bold green]Welcome [/bold green]", "[bold green]to [/bold green]", "[bold green]anantdark's [/bold green]", "[bold green]Hangman [/bold green]", "[bold green]game.[/bold green]"]:
        print(word, end=" ")
        sleep(0.5)
    print()


def hangman(word):
    welcome_screen()
    system("clear")
    used_letters = []
    lives = 6
    board = "*"*len(word)

    def prompt_with_message(message):
        print(f"{message}\nYou still have {lives} lives. Guess again!")
        return input()

    while lives:
        print(f'You have {lives} lives. Guess a word. \nCurrent board',
            f'(guessed letters: {" ".join(used_letters)})' if used_letters else '',
            f'\n{board}')
        guess = input()
        # If guess is more than 1 character, prompt to try again
        while len(guess) != 1:
            guess = prompt_with_message("You can only guess with 1 character")
        # If character exist in word, then don't lose a life
        character_exist = False
        # If the player has reused a guess, prompt to try again
        while guess in used_letters:
            guess = prompt_with_message("You have already used this letter.")
        
        used_letters += guess
        
        for i in range(len(word)):
            if guess == word[i]:
                # Keep everything before and after index but replace at index
                board = board[:i] + guess + board[i+1:]
                character_exist = True
        if not character_exist:
            lives -= 1
        print(board)
        system('clear')
        # If any character is missing, continue (go back to top of while loop
        # and skipping win prompt
        completed_word = True
        for char in board:
            if char == "*":
                completed_word = False
                break
        if completed_word:
            break

    if lives == 0:
        print(f'You lost all your lives\U00002764 \U00002639 The word is {word}')
    else:
        print(f'You win\U0001F389! The word is {word}')


if __name__ == "__main__":
    current_word = random_word()
    hangman(current_word)
