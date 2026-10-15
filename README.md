# Hangman-Game
A simple Hangman game made using Python where players try to guess a hidden word one letter at a time. This project helped me practice basic Python concepts like loops, conditions, strings, lists, and random selection.

# About the Project

Hangman is a classic word-guessing game. In this version, the computer randomly selects a word from a predefined list of five words, and the player tries to guess it by entering letters. Each correct guess reveals the matching letters in the word, while each incorrect guess brings the player closer to the limit of six mistakes. The game ends when the player guesses the word correctly or reaches the maximum number of incorrect guesses.

# Features
Randomly selects a word from a list of five words.

Allows the player to guess one letter at a time.

Displays correctly guessed letters and hidden letters.

Tracks previously guessed letters and incorrect attempts.

Allows a maximum of six incorrect guesses.

Checks for repeated letters and invalid input.

Displays a message when the player wins or loses.

# Technologies Used
Python 3

Random module

While loops

If-else statements

Strings and lists

# How to Run the Game
Make sure Python 3 is installed on your computer.

Clone this repository or download the project files.

Open the project folder in your terminal.

Run the following command:
   python hangman.py


# How to Play
Start the program.

The computer will select a secret word.

Enter one alphabet letter when prompted.

If the letter is correct, it will appear in the word.

If the letter is incorrect, your incorrect guess count will increase.

Guess the complete word before reaching six incorrect guesses to win.
