#!/bin/bash


# check if a filename was provided

if [ "$#" -ne 1 ]; then
	echo "Usage: $0 <filename>"
	exit 1
fi


filename="$1"


#check if hte file exists and is readable

if [ -f "$filename" ] && [ -r "$filename" ]; then
	echo "Contents of '$filename':"
	cat "$filename"
else
	echo "Error: File '$filename' not found or not readable"
	exit 1
fi
