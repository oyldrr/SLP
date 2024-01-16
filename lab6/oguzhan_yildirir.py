import random

def read_capitals(filename='capitals.txt'):
    with open(filename, 'r') as file:
        capitals = [line.strip() for line in file]
    return capitals

def choose_capital(capitals):
    return random.choice(capitals)

def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_ "
    return display

def hangman():
    guessed_letters = []
    max_attempts = 6
    attempts = 0
    
    capitals = read_capitals()
    selected_capital = choose_capital(capitals)

    print("\nWelcome to Hangman! Try to guess the name of the capital.")
    while True:
        print("---")
        current_display = display_word(selected_capital, guessed_letters)
        print("\nCurrent word: " + current_display)
        
        if current_display == selected_capital:
            print("\nCongratulations! You guessed the capital: " + selected_capital)
            break

        guess = input("\nGuess a letter: ").upper()

        if guess.isalpha() and len(guess) == 1:
            if guess in guessed_letters:
                print("\nYou've already guessed that letter. Try again.")
            elif guess in selected_capital:
                print("\nGood guess!")
                guessed_letters.append(guess)
            else:
                print("\nIncorrect guess. Try again.")
                guessed_letters.append(guess)
                attempts += 1
                print("\nAttempts left: {}".format(max_attempts - attempts))
                if attempts == max_attempts:
                    print("\nSorry, you've run out of attempts. The capital was: " + selected_capital)
                    break
        else:
            print("\nInvalid input. Please enter a single letter.")

if __name__ == "__main__":
    hangman()
