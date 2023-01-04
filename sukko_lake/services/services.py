import os
import smtplib
import ssl

from dotenv import load_dotenv

from sukko_lake.services.text import Messages

load_dotenv()


SMTP_SERVER = 'smtp.mail.ru'
SSL_PORT = 465
SENDER_EMAIL = os.getenv('SENDER_EMAIL')
RECEIVER_EMAIL = os.getenv('RECEIVER_EMAIL')
MAIL_TOKEN = os.getenv('MAIL_TOKEN')


def get_message(client_name: str, client_phone: str) -> bytes:
    """Get message from template into which substituted
    client name and client phone"""
    template = Messages.NewApplication.value
    return template.substitute(
        client_name=client_name, client_phone=client_phone
    ).encode('utf-8')


def send_alert_email(client_name: str, client_phone: str) -> None:
    """Send email to owner with alert about new application has been left"""
    ssl_context = ssl.create_default_context()
    message = get_message(client_name, client_phone)
    with smtplib.SMTP_SSL(
            SMTP_SERVER, SSL_PORT, context=ssl_context) as server:
        server.login(SENDER_EMAIL, MAIL_TOKEN)
        server.sendmail(SENDER_EMAIL, RECEIVER_EMAIL, message)


def is_true_phone_number(phone: str) -> bool:
    """Validation phone number. If validation is False,
    application won't be added to db"""
    normalize_number = phone.replace('-', '').replace(' ', '')
    print(normalize_number)
    return normalize_number.isdigit() and len(normalize_number) == 10
