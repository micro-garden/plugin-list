#!/bin/sh
tmp_repos="/tmp/github_repos.txt"
tmp_body="/tmp/index_body._md"

echo "Searching GitHub Repos for 'language:lua micro' ..."
python3 search_github_repos.py > "$tmp_repos"
echo "Parsing repo.json and Generating Markdown Body ..."
cat "$tmp_repos" | python3 parse_repo_json.py > "$tmp_body"
echo "Updating index.md ..."
cat index_head._md "$tmp_body" index_tail._md >index.md

echo "Done"
