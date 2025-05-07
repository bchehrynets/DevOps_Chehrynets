#!/bin/bash


#check if a filename is provided

if [ "$#" -ne 1 ]; then
	echo "Usage: $0 <filename>"
	exit 1
fi


# assign filename

file="$1"


# check if the file exists

if [ ! -f "$file" ]; then
	echo "Error: File '$file' not found."
	exit 1
fi

# count and print the number of lines

line_count=$(wc -l "$file")
echo "Number of lines in '$file': $line_count"
