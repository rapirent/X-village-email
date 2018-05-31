import csv
import smtplib
from email.message import EmailMessage
from argparse import ArgumentParser


parser = ArgumentParser()
parser.add_argument('-s', '--sendemail', default='x.village.share@gmail.com')
parser.add_argument('-f', '--filename', default='check.csv')
parser.add_argument('-t', '--time', default='6/10')
parser.add_argument('-p', '--password', default='')
args = parser.parse_args()
date = args.time

print('start to send email...')

with open(args.filename, newline='') as csvfile:
    csv_reader = csv.DictReader(csvfile)

    for row in csv_reader:
        name = row['name']
        receive_email = row['email']
        type = row['type']

        content = name + ''' 同學 您好，

X-Village已收到您的報名資訊(報名'''+ type +''')，後續若有特殊因素需調整資料，請回信此封郵件。   報名資訊審核通過後我們將另行通知，謝謝。

Best regards,
X-Village'''
        print(name)
        msg = EmailMessage()
        msg.set_content(content)
        msg['Subject'] = '[X-Village] 已收到您的報名'
        msg['From'] = args.sendemail
        msg['To'] = receive_email

        server = smtplib.SMTP('smtp.gmail.com:587')
        server.ehlo()
        server.starttls()
        server.login(args.sendemail, args.password)
        server.ehlo()
        server.send_message(msg)
        server.quit()

print('finish...')


