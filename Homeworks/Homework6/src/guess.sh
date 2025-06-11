#!/bin/bash

secret=$((RANDOM % 100 + 1))
attempts=5

echo "Guess a number between 1 and 100. You have $attempts attempts."

for ((i=1; i<=attempts; i++)); do
    read -p "Attempt $i: " guess

    if ! [[ "$guess" =~ ^[0-9]+$ ]]; then
        echo "Please enter a valid number."
        ((i--))
        continue
    fi

    if (( guess == secret )); then
        echo "Congratulations! You guessed the correct number."
        exit 0
    elif (( guess < secret )); then
        echo "Too low."
    else
        echo "Too high."
    fi
done

echo "Sorry, you've run out of attempts. The correct number was $secret."

