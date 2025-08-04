import os
import sys
import json
import glob
import re
import html

REPO_DIR = "repo"


def extract_user_repo(filename):
    base = os.path.basename(filename)
    if not base.endswith(".json") or "@" not in base:
        return None, None
    repo_part, user_part = base[:-5].split("@", 1)
    return user_part, repo_part


def supports_micro_v2(entry):
    try:
        versions = entry.get("Versions", [])
        version = versions[0]
        require = version.get("Require", {})
        micro_ver = require.get("micro", "")
        return bool(re.match(r"^\s*>=\s*2", micro_ver))
    except Exception:
        return False


def main():
    files = sorted(glob.glob(os.path.join(REPO_DIR, "*.json")))
    entries = []

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
            if "Name" not in entry or "Description" not in entry:
                continue

            name = html.escape(entry["Name"])
            desc = html.escape(entry["Description"])
            license_str = html.escape(entry.get("License", "Unknown"))
            micro_v2 = "✅" if supports_micro_v2(entry) else "❌(may still work)"

            entries.append(
                {
                    "name": name,
                    "desc": desc,
                    "license": license_str,
                    "micro_v2": micro_v2,
                    "url": url,
                }
            )

    for entry in sorted(entries, key=lambda x: x["name"].lower()):
        print(f"* [{entry['name']}]({entry['url']}) : {entry['desc']}  ")
        print(f"  License: {entry['license']}, micro v2+: {entry['micro_v2']}")


if __name__ == "__main__":
    main()
