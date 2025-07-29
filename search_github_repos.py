import os
import requests
from dotenv import load_dotenv

load_dotenv()
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")

if not GITHUB_TOKEN:
    raise RuntimeError("GITHUB_TOKEN is not set in the .env file.")

QUERY = "language:lua micro"
PER_PAGE = 100
MAX_PAGES = 10


def search_github_repositories(query, token, max_pages=10, per_page=100):
    url = "https://api.github.com/search/repositories"
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github+json",
        "User-Agent": "python-script",
    }

    all_items = []

    for page in range(1, max_pages + 1):
        params = {
            "q": query,
            "per_page": per_page,
            "page": page,
        }

        response = requests.get(url, headers=headers, params=params)
        if response.status_code != 200:
            print(f"Error: {response.status_code} {response.text}")
            break

        data = response.json()
        items = data.get("items", [])
        if not items:
            break

        all_items.extend(items)

        if len(all_items) >= data.get("total_count", 0):
            break

    return all_items


def main():
    repos = search_github_repositories(QUERY, GITHUB_TOKEN, MAX_PAGES, PER_PAGE)

    for repo in repos:
        print(repo["html_url"])


if __name__ == "__main__":
    main()
