import os
import json
import glob
import sys

REPO_DIR = "repo"


def extract_user_repo(filename):
    # repo/micro-colorswitcher-plugin@akikareha.json -> ("akikareha", "micro-colorswitcher-plugin")
    base = os.path.basename(filename)
    if not base.endswith(".json") or "@" not in base:
        return None, None
    repo_part, user_part = base[:-5].split("@", 1)
    return user_part, repo_part


def main():
    files = sorted(glob.glob(os.path.join(REPO_DIR, "*.json")))

    for filepath in files:
        user, repo = extract_user_repo(filepath)
        if not user or not repo:
            continue

        url = f"https://github.com/{user}/{repo}"

        try:
            with open(filepath, "r", encoding="utf-8") as f:
                data = json.load(f)
        except Exception as e:
            print(f"# Failed to parse {filepath}: {e}", file=sys.stderr)
            continue

        if not isinstance(data, list):
            continue

        for entry in data:
            if not isinstance(entry, dict):
                continue
            if "Name" in entry and "Description" in entry:
                name = entry["Name"]
                desc = entry["Description"]
                print(f"* [{name}]({url}) : {desc}")


if __name__ == "__main__":
    main()
