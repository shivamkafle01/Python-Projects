Description:
A simple number guessing game where players try to guess a randomly generated number between 1 and 100. Players receive hints about whether their guess is too high or too low and aim to find the number in the fewest guesses possible.
Presentation:
Title: Number Guessing Game
Description:
Challenge yourself with this fun number guessing game! Guess the secret number between 1 and 100 and see how quickly you can find it. Get hints along the way to guide your guesses.
Instructions:
1. Run the Python script.
2. Enter your guess when prompted.
3. Receive feedback on whether your guess is too high or too low.
4. Keep guessing until you find the correct number.
5. Enjoy the satisfaction of winning!

import random

def play_game():
    number_to_guess = random.randint(1, 100)
    guess_count = 0
    while True:
        guess = int(input("Guess a number between 1 and 100: "))
        guess_count += 1
        if guess < number_to_guess:
            print("Too low!")
        elif guess > number_to_guess:
            print("Too high!")
        else:
            print(f"Congratulations! You found the number in {guess_count} guesses.")
            break

if __name__ == "__main__":
    play_game()

