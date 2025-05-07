#!/bin/bash


#create an array of fruits

fruits=("Apple" "Papaya" "Cherry" "Banana" "Strawberry")


# loop through the array and print each fruit


for fruit in "${fruits[@]}"; do
	echo "$fruit"
done
