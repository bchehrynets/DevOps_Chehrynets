#!/bin/bash


# ask filename

read -p "Enter the filename to check: " filename

#check if the file exists


if [ -f "$filename" ]; then
	echo "The file '$filename' exists."
else
	echo "The file '$filename' does not exist."

fi
