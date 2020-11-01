import smtplib
import api


def send_email(target_user: str, send_to: str):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(api.get_email_from(), api.get_email_password())
    subject = f'{target_user} created a new repository!'
    repositories_link = f'https://github.com/{target_user}?tab=repositories'
    body = f'Hey there!\n {target_user} created a new repository. Check it out: {repositories_link}'
    message = f'Subject: {subject}\n\n{body}'
    server.sendmail(api.get_email_from(), send_to, message)
    print(f'Sending e-mail to {send_to}.')
    server.quit()
