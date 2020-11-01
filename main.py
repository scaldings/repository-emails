import api
import send_email
from time import sleep

repo_init = False
last_repositories = 0

if __name__ == '__main__':
    if repo_init is False:
        last_repositories = api.get_repositories_count(api.get_target_user())
        repo_init = True
    while True:
        current_repositories = api.get_repositories_count(api.get_target_user())
        if current_repositories is not last_repositories:
            if current_repositories > last_repositories:
                send_email.send_email(api.get_target_user(), api.get_email_to())
            last_repositories = current_repositories
        print('Sleeping for 5 minutes / 300 seconds')
        sleep(300)
