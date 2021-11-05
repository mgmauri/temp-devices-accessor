import smtplib
from email.message import EmailMessage

from src.core.configs import EmailConfig

sender_email = EmailConfig.config.user()
password = EmailConfig.config.password()


def send_warning_to_gmail_user(to_user: str):
    msg = EmailMessage()
    msg["Subject"] = "Silicon Thermal Server Warning"
    msg["From"] = sender_email
    msg["To"] = f"{to_user}@gmail.com"
    msg.set_content("Silicon Thermal was set to an above threshold temperature")
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(user=sender_email, password=password)
        smtp.send_message(msg)
