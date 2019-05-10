from smtplib import SMTP
from email.header import Header
from email.mime.text import

def main():
    # Modify the follow mail senders and recipients
    sender = '@qq.com'
    receiver = ['@qq.com','@qq.com']
    message = MIMEText('Sample code for sending email with python','plain','utf-8')
    message['From'] = Header('Zhang San', 'utf-8')
    message['To'] = Header('Li Si', 'utf-8')
    smtper = SMTP('smtp.126.com')
