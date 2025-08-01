import sys
import os
import glob
import requests

REPO_DIR = "repo"


def clean_repo_dir():
    json_files = glob.glob(os.path.join(REPO_DIR, "*.json"))
    for path in json_files:
        try:
            os.remove(path)
        except Exception as e:
            print(f"# Failed to remove {path}: {e}", file=sys.stderr)


def fetch_and_save(repo_url):
    if not repo_url.startswith("https://github.com/"):
        return

    parts = repo_url.strip().removeprefix("https://github.com/").split("/")
    if len(parts) < 2:
        return

    user, repo = parts[:2]

    for branch in ["main", "master"]:
        raw_url = f"https://raw.githubusercontent.com/{user}/{repo}/{branch}/repo.json"
        try:
            response = requests.get(raw_url, timeout=5)
            if response.status_code == 200:
                filename = f"{repo}@{user}.json"
                path = os.path.join(REPO_DIR, filename)
                with open(path, "w", encoding="utf-8") as f:
                    f.write(response.text)
                print(f"# Saved: {path}", file=sys.stderr)
                return
        except Exception as e:
            print(f"# Error fetching {raw_url}: {e}", file=sys.stderr)

    print(f"# repo.json not found: {repo_url}", file=sys.stderr)


def main():
    clean_repo_dir()

    for line in sys.stdin:
        repo_url = line.strip()
        if not repo_url:
            continue
        fetch_and_save(repo_url)


if __name__ == "__main__":
    main()
