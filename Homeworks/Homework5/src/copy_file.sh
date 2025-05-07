#!/bin/bash

# check if exactly two arguments are passed

if [ "$#" -ne 2 ]; then
	echo "Usage: $0 source_file destination_path"
	exit 1
fi

# assign arguments to variables

source_file="$1"
destination_path="$2"


# copy the file

if [ -f "$source_file" ]; then
	cp "$source_file" "$destination_path"
	echo "File copied from '$source_file' to '$destination_path'"
else
	echo "Source file '$source_file' does not exist"
	exit 1
fi
