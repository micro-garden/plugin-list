#!/bin/sh
echo "Searching GitHub Repos for 'language:lua micro' ..."
python3 search_github_repos.py >github_repos.txt
echo "Fetching repo.json ..."
cat github_repos.txt | python3 fetch_repo_json.py
echo "Done"
