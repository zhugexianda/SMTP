__author__ = 'xianda'

from email.mime.text import MIMEText
import smtplib

msg = MIMEText('hello,you are great, come on!', 'plain', 'utf-8')
from_addr = input('From:')
password = input('password:')
to_addr = input('To:')
smtp_server = input('server:')

server = smtplib.SMTP_SSL(smtp_server, 465)
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], str(msg))
server.quit()
