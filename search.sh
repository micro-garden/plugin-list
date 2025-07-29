#!/bin/sh
echo "Searching GitHub Repos for 'language:lua micro' ..."
python3 search_github_repos.py >github_repos.txt
echo "Parsing repo.json and Generating Markdown Body ..."
cat github_repos.txt | python3 parse_repo_json.py | sort >index_body._md
echo "Done"
