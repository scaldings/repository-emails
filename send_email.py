import smtplib


def send_email(target_user: str, send_to: str):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    text = open('information.txt', 'r').read().split('\n')
    server.login(text[0], text[1])
    subject = f'{target_user} created a new repository!'
    repositories_link = f'https://github.com/{target_user}?tab=repositories'
    body = f'Hey there! {target_user} created a new repository. Check it out: {repositories_link}'
    message = f'Subject: {subject}\n\n{body}'
    server.sendmail(text[0], send_to, message)
    server.quit()
