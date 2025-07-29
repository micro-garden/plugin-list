import sys
import requests
import json


def fetch_repo_json(repo_url):
    if not repo_url.startswith("https://github.com/"):
        print(f"# Skipping invalid URL: {repo_url}", file=sys.stderr)
        return None

    parts = repo_url.strip().removeprefix("https://github.com/").split("/")
    if len(parts) < 2:
        print(f"# Invalid repo URL format: {repo_url}", file=sys.stderr)
        return None

    user, repo = parts[:2]

    for branch in ["master", "main"]:
        raw_url = f"https://raw.githubusercontent.com/{user}/{repo}/{branch}/repo.json"
        try:
            response = requests.get(raw_url, timeout=5)
            if response.status_code == 200:
                return response.json()
        except Exception as e:
            print(f"# Error fetching {raw_url}: {e}", file=sys.stderr)

    print(f"# repo.json not found for {repo_url}", file=sys.stderr)
    return None


def main():
    for line in sys.stdin:
        repo_url = line.strip()
        if not repo_url:
            continue

        data = fetch_repo_json(repo_url)
        if not data:
            continue

        if not isinstance(data, list):
            print(f"# repo.json is not a list in {repo_url}", file=sys.stderr)
            continue

        for entry in data:
            if not isinstance(entry, dict):
                continue
            if "Name" in entry and "Description" in entry:
                name = entry["Name"]
                desc = entry["Description"]
                print(f"* [{name}]({repo_url}) : {desc}")
            else:
                print(
                    f"# Skipping entry without Name or Description in {repo_url}",
                    file=sys.stderr,
                )


if __name__ == "__main__":
    main()
