import random

def guess_the_number():
        correct_number = random.randint(1,100)
        max_attempts = 5

        print("Guess the number between 1 and 100. You have 5 attempts")

        for attempt in range(1, max_attempts +1):
            try:
                guess = int(input(f"Attempt {attempt}: Enter your guess: "))
            except ValueError:
                print("Invalid input. Please enter an integer.")
                continue

            if guess == correct_number:
                print("Congratilations! You guessed the right number.")
                return
            elif guess < correct_number:
                print("Too low.")
            else:
                print("Too high.")

        print(f"Sorry, you have run out of attempts. The correct number was {correct_number}.")

# Call the function to run the game
guess_the_number()
