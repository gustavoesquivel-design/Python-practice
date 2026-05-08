import random


def get_guess():
   while True:
        try:
            guess = int(input("Enter your guess: "))
            if guess < 1 or guess > 15:
                print("Try again! Remember the number must bebetween 1 and 15.")
                return get_guess()  # Recursively ask for a valid guess
            return guess
        except ValueError:
            print("Invalid input. Please enter a number.")
            return get_guess()  # Recursively ask for a valid guess

def main():
    name = input("What's your name? ")
    print(f"Welcome, {name}! to the Guessing Game!")
    print("Try to guess the number between 1 and 15.")
    number_to_guess = random.randint(1, 15)  # This is the number you need to guess
    attempts = 0
    guessed_correctly = False

    while not guessed_correctly:
        guess = get_guess()
        attempts += 1

        if guess < number_to_guess:
            print("Too low! Try again.")
        elif guess > number_to_guess:
            print("Too high! Try again.")
        else:
            guessed_correctly = True
            print(f"Congratulations, {name}! You've guessed the number in {attempts} attempts.")

main()
