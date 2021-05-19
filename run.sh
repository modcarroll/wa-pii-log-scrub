#!/bin/sh

echo "🧹 Starting scrubber"

for entry in "data"/*
do
  python3 main.py $entry
done

echo "✅ Complete"
