import csv
import smtplib
from email.message import EmailMessage
from argparse import ArgumentParser


parser = ArgumentParser()
parser.add_argument('-s', '--sendemail', default='x.village.share@gmail.com')
parser.add_argument('-f', '--filename', default='invitation.csv')
parser.add_argument('-t', '--time', default='6/10')
parser.add_argument('-p', '--password', default='')
args = parser.parse_args()
date = args.time

print('start to send email...')

with open(args.filename, newline='') as csvfile:
    csv_reader = csv.DictReader(csvfile)

    for row in csv_reader:
        teacher = row['teacher']
        title = row['title']
        student = row['student']
        recommender = teacher + ' ' + title
        receive_email = row['email']

        content = recommender + '''您好， 我們是X-Village。
X-Village是國立成功大學的實驗教育計畫，由教育部支持並隸屬於資通訊軟體創新人才推升計畫(ITSA)的先導計劃，旨在培育跨領域能力及跨域交流。

我們收到學生 ''' + student + ''' 提出希望您編寫修課推薦信的邀請，這部分於下方 Google 表單內填寫即可。 此外推薦信結果不會經過學生，推薦人可以放心如實填寫，謝謝。

填寫截止日期至： ''' + date + '''

Google 表單連結：

X-Village 簡介：https://sites.google.com/view/x-village

Best regards,
X-Village'''
        msg = EmailMessage()
        msg.set_content(content)
        msg['Subject'] = '學生 ' + student + ' 邀請 ' + recommender + '填寫 X-Village 學生推薦信'
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


