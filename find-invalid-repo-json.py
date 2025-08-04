import os
import json
import glob

REPO_DIR = "repo"


def extract_user_repo(filename):
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
            print(f"* {url} : Parse Error")
            continue

        if not isinstance(data, list):
            print(f"* {url} : Not a List")
            continue

        for entry in data:
            if not isinstance(entry, dict):
                print(f"* {url} : No Dicts")
                continue
            found = False
            if "Name" not in entry:
                print(f"* {url} : No Name")
                found = True
            if "Description" not in entry:
                print(f"* {url} : No Description")
                found = True
            if found:
                continue


if __name__ == "__main__":
    main()
