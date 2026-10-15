import random

# Words and their hints
words = {
    "nobita": "a zero marks cartoon character.",
    "rainbow": "A dispersion of white light.",
    "shinchan": "I'll protect you, Himawari",
    "science": "The systematic study of the natural world.",
    "quantum": "The study of the smallest."
}

# Select a random word
word = random.choice(list(words.keys()))

# Get the matching hint
hint = words[word]

guessed_letters = []
wrong_guesses = 0
max_attempts = 6

print("Welcome to the Hangman Game!")
print("Hint:", hint)
print("Number of letters:", len(word))

while wrong_guesses < max_attempts:

    display_word = ""

    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word)
    print("Incorrect guesses:", wrong_guesses, "/", max_attempts)

    if all(letter in guessed_letters for letter in word):
        print("Congratulations! You guessed the word:", word)
        break

    guess = input("Enter one letter: ").lower().strip()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single letter.")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter!")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print("Correct guess!")
    else:
        wrong_guesses += 1
        print("Wrong guess!")

if wrong_guesses == max_attempts:
    print("Game over! The word was:", word)
