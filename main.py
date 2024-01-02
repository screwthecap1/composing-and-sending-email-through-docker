from email.message import EmailMessage
import smtplib  # отправка сообщения
from string import Template
from pathlib import Path

my_email = EmailMessage()

html_template = Template(Path("templates/index.html").read_text())
html_content = html_template.substitute({'name': 'Klim', 'date': 'next week'})

my_email['from'] = 'Klim'
my_email['to'] = 'bro@mail.ru'
my_email['subject'] = 'I wanna make it for real'
my_email.set_content(html_content, 'html')

with smtplib.SMTP(host='localhost', port=2525) as smtp_server:
    smtp_server.ehlo()
    # smtp_server.starttls()
    # smtp_server.login('username', 'password')
    smtp_server.send_message(my_email)
    print("Email was successfully sent!")
