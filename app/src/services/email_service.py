import smtplib

class EmailService:
    def __init__(self, from_addr: str, password: str):
        self.from_addr = from_addr
        self.password = password

    def send_email(self, message, receiver_emails: list):
        smtp = smtplib.SMTP('smtp.gmail.com', 587)
        smtp.starttls()
        smtp.login(user=self.from_addr, password=self.password)
        smtp.sendmail(from_addr=self.from_addr, to_addrs=receiver_emails, msg=message)
        smtp.quit()

