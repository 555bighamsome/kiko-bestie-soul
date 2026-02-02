#!/bin/bash
# V14 Soul Sync Setup Helper

echo "--- KikoBestie Soul Sync Setup ---"
echo "1. Go to https://github.com/new"
echo "2. Create a PRIVATE repository named: kiko-bestie-soul"
echo "3. Copy the SSH remote URL (looks like git@github.com:USERNAME/kiko-bestie-soul.git)"
echo "4. Paste the URL here and press Enter:"
read REMOTE_URL

if [ -z "$REMOTE_URL" ]; then
    echo "Error: No URL provided."
    exit 1
fi

cd /Users/mac/.openclaw/workspace
git remote add origin "$REMOTE_URL"
git branch -M main
git push -u origin main

echo "Done! Your soul is now syncing to the cloud 24/7."
