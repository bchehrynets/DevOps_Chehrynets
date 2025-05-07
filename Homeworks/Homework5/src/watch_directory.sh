#!/bin/bash

WATCH_DIR="$HOME/watch"

# create the directory if it doesn't exist

mkdir -p "$WATCH_DIR"

# watch for new files

inotifywait -m -e create --format "%f" "$WATCH_DIR" | while read filename; do
	full path="$WATCH_DIR/$filename"

	#wait for the file to be fully written
	sleep 1

	if [ -f "$fullpath" ]; then
		echo "New file detected: $filename"
		echo "Content:"
		cat "$fullpath"


		# rename the file
		mv "$fullpath" "$fullpath.back"
	fi
done
