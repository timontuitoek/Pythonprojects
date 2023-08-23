import random

def choose_word():
    words = ['apple', 'banana', 'cherry', 'dog', 'elephant', 'fruits', 'grape', 'honey', 'icecream', 'jelly']
    return random.choice(words)

def display_word(word, guessed_letters):
    display = ''
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += '_'
    return display

def hangman():
    word = choose_word()
    guessed_letters = []
    attempts = 6

    print("Welcome to Hangman!")

    while True:
        # Display the word with underscores for unguessed letters
        print("\nWord:", display_word(word, guessed_letters))

        # Prompt the user for a guess
        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            # Inform the user if they've already guessed that letter
            print("You already guessed that letter.")
        elif guess in word:
            # Add the guessed letter to the list and check if the whole word is guessed
            guessed_letters.append(guess)
            if word == display_word(word, guessed_letters):
                print("\nCongratulations! You guessed the word:", word)
                break
        else:
            # Incorrect guess - decrease attempts and check if the game is lost
            guessed_letters.append(guess)
            attempts -= 1
            print("Incorrect guess. You have", attempts, "attempts left.")
            if attempts == 0:
                print("\nSorry, you're out of attempts. The word was:", word)
                break

# Start the Hangman game
hangman()
