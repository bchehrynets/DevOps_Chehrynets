#!/bin/bash

WATCH_DIR="$HOME/watch"
mkdir -p "$WATCH_DIR"

inotifywait -m -e create --format '%f' "$WATCH_DIR" | while read FILE; do
    FILE_PATH="$WATCH_DIR/$FILE"
    if [ -f "$FILE_PATH" ]; then
        echo "=== New File Detected: $FILE ==="
        cat "$FILE_PATH"
        mv "$FILE_PATH" "$FILE_PATH.back"
        echo "--- Renamed to $FILE.back ---"
    fi
done

