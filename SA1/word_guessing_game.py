'''Start by creating a new Python file and saving it as "word_guessing_game.py" or you can just use the filename above.

Open the "words.txt" file, which contains a list of words that will be used in the game. Each word should be on a
separate line in the file.

Create a function to randomly select a word from the "words.txt" file.

Create a function to display the word to the player. This function should replace all letters in the word with
underscores, except for letters that have already been guessed.

Create a function to get the player's guess. This
function should ask the player to enter a letter and validate the input to make sure it is a single letter.

Create a main function to run the game. The main function should use the previously defined functions to select a word,
display it to the player, and prompt the player for guesses until the word is guessed or the player runs out of
guesses. Finally, call the main function to run the game. '''
from random import choice


def random_word_function(choices):
    return choice(choices)


def underscore_function(random_word, letters_guessed, guesses, guess_let):
    letters_guessed.append(guess_let)
    update = ' '.join(letter if letter in letters_guessed else '_' for letter in random_word)
    print(update)
    if guess_let not in random_word:
        guesses -= 1
    return [letters_guessed, update, guesses]


def user_input():
    while True:
        guess_let = input("Guess a letter: ").lower()
        if len(guess_let) == 1 and guess_let.isalpha():
            return guess_let


def main():
    with open('words.txt', 'r') as file:
        contents = file.read()
        words = contents.split()
        random_word = random_word_function(words)
        # print(random_word)
        guesses = 8
        letters_guessed = []
        guess_let = ''
        update = '_'
        underscore_function(random_word=random_word, letters_guessed=letters_guessed, guesses=guesses,
                            guess_let=guess_let)
        while '_' in update:
            guess_let = user_input()
            data = underscore_function(random_word=random_word, letters_guessed=letters_guessed, guesses=guesses,
                                       guess_let=guess_let)
            letters_guessed = data[0]
            update = data[1]
            if data[2] < guesses:
                guesses = data[2]
                print(f'Incorrect. {data[2]} guesses remaining.')
            else:
                print('Correct!')
            if guesses == 0:
                break
        if '_' not in update:
            print(f'Congratulations! You have guessed all the letters of the word "{random_word}"')
        if guesses == 0:
            print(f'Sorry, you lose. The word was "{random_word}"')


if __name__ == '__main__':
    main()