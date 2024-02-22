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

