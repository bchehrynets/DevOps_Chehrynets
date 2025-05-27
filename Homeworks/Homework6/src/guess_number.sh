#!/bin/bash

# Generate a random number between 1 and 100
target=$(( RANDOM % 100 + 1 ))
attempts=0
max_attempts=5

echo "Guess the number between 1 and 100. You have $max_attempts attempts."

while (( attempts < max_attempts )); do
    read -p "Attempt $((attempts+1)): " guess

    # Check if input is a valid number
    if ! [[ "$guess" =~ ^[0-9]+$ ]]; then
        echo "Please enter a valid integer."
        continue
    fi

    ((attempts++))

    if (( guess == target )); then
        echo "Congratulations! You guessed the correct number: $target"
        exit 0
    elif (( guess < target )); then
        echo "Too low."
    else
        echo "Too high."
    fi
done

echo "Sorry, you've used all your attempts. The correct number was $target."

