# email
a python simple email script for invitation email and register-check of x-village

***YOU SHOULD ADD GOOGLE FORM LINK TO THE INVITATION CONTENT VARIABLE***

```
您好， 我們是X-Village。
X-Village是國立成功大學的實驗教育計畫，由教育部支持並隸屬於資通訊軟體創新人才推升計畫(ITSA)的先導計劃，旨在培育跨領域能力及跨域交流。

我們收到學生  提出希望您編寫修課推薦信的邀請，這部分於下方 Google 表單內填寫即可。 此外推薦信結果不會經過學生，推薦人可以放心如實填寫，謝謝。

填寫截止日期至：

Google 表單連結：

X-Village 簡介：https://sites.google.com/view/x-village

Best regards,
X-Village
```

# requirements
python3
# usage

1. edit the csv file to specify the receiver

2. run the script
```sh
$ python invitation.py [-s SENDEMAIL] [-f FILENAME] [-t TIME] [-p PASSWORD]
$ python check.py [-s SENDEMAIL] [-f FILENAME] [-t TIME] [-p PASSWORD]
```

- `SENDEMAIL` for your sender email address of SMTP server (default to gmail) and account
- `FILENAME` for your content csv files (e.g. `input.csv`)
- `TIME` for your content time (e.g. `6/10`)
- `PASSWORD` for your sender email account password

# author
kuoteng
# license
MIT
