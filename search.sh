#!/bin/sh
echo "Searching GitHub Repos for 'language:lua micro' ..."
python3 search-github-repos.py >github-repos.txt
echo "Fetching repo.json ..."
cat github-repos.txt | python3 fetch-repo-json.py
echo "Done"
