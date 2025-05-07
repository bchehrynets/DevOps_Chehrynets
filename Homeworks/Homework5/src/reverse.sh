#!/bin/bash

#ask the user to enter a sentence

read -p "Enter a sentence: " sentence

# reverse the sentence word by word

reversed=$(echo "$sentence" | awk '{for(i=NF;i>0;i--) printf "%s ", $i; print ""}')

#output the reversed sentence

echo "Reversed sentence: $reversed"


