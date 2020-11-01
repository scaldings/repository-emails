import requests
from os import environ


def get_repositories_count(target_user: str):
    url = f'https://api.github.com/users/{target_user}'
    repo_count = requests.get(url).json()['public_repos']
    return repo_count


def get_target_user():
    return environ['TARGET_USER']


def get_email_to():
    return environ['EMAIL_TO']


def get_email_from():
    return environ['EMAIL_FROM']


def get_email_password():
    return environ['EMAIL_PASSWORD']
