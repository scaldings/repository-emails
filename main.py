import api
import send_email
from time import sleep

repos_init = False
last_repositories = 0


def get_target():
    information = open('information.txt', 'r').read().split('\n')
    return str(information[3])


def get_email():
    information = open('information.txt', 'r').read().split('\n')
    return str(information[2])


if __name__ == '__main__':
    if repos_init is False:
        last_repositories = api.get_repositories_count(get_target())
        repos_init = True
    while True:
        current_repositories = api.get_repositories_count(get_target())
        if current_repositories is not last_repositories:
            if current_repositories > last_repositories:
                send_email.send_email(get_target(), get_email())
            last_repositories = current_repositories
        sleep(1800)
