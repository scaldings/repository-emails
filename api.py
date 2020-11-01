import requests


def get_repositories_count(target_user: str):
    url = f'https://api.github.com/users/{target_user}'
    repo_count = requests.get(url).json()['public_repos']
    return repo_count
