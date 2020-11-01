import api
import send_email
from time import sleep

repos_init = False
last_repositories = 0

if __name__ == '__main__':
    if repos_init is False:
        last_repositories = api.get_repositories_count(api.get_target_user())
        repos_init = True
    while True:
        current_repositories = api.get_repositories_count(api.get_target_user())
        if current_repositories is not last_repositories:
            if current_repositories > last_repositories:
                send_email.send_email(api.get_target_user(), api.get_email_to())
            last_repositories = current_repositories
        print('Sleeping for 15 minutes / 900 seconds')
        sleep(900)
