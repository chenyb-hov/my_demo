from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
import smtplib, ssl
from email.header import Header
from email.utils import parseaddr, formataddr
from email import encoders

#网易邮箱
# content = 'Python Send Mail !'
# title = 'Python SMTP Mail Test'
# message = MIMEText(content, 'plain', 'utf-8')
# message['Subject'] = title
# from_addr = input('From: ')
# password = input('password: ')
# to_addr = input('To: ')
# # smtp.163.com
# #smtp_server = input('SMTP server: ')
# smtp_host = 'smtp.163.com'
# smtp_host1 = 'smtp.gmail.com'
# import smtplib
# server = smtplib.SMTP(smtp_host1, 25)
# # server = smtplib.SMTP_SSL(smtp_host1, 587)
# server.set_debuglevel(1)
# server.ehlo()
# server.starttls()
# server.login(from_addr, password)
# server.sendmail(from_addr, [to_addr], message.as_string())
# server.quit()

# port = 587
# smtp_server = 'smtp.gmail.com'
# sender_email = 'chenyb101500@gmail.com'
# receiver_email = 'ningchen@google.com'
# password = input('password: ')
# message = '''\
# Subject:Hi there
# This message is sent from Python.'''
#
# context = ssl.create_default_context()
# with smtplib.SMTP(smtp_server, port) as server:
#     # server.ehlo()
#     server.starttls()
#     #server.starttls(context=context)
#     # server.ehlo()
#     server.set_debuglevel(1)
#     server.login(sender_email, password)
#     server.sendmail(sender_email, [receiver_email], message.as_string())



# def _format_addr(s):
#     name, addr = parseaddr(s)
#     return formataddr((Header(name, 'utf-8').encode(), addr))
#
# from_addr = 'msg44057637@163.com'
# password = input("Passoword: ")
# to_addr = '782924856@qq.com'
# smtp_server = 'smtp.163.com'
# msg = MIMEMultipart()
# # 同时支持plain和html
# # msg = MIMEMultipart('alternative')
# msg.attach(MIMEText('<html><body><h1>Hello</h1>' +
#     '<p>send by <a href="http://www.python.org">Python</a>...</p><img src="cid:0"/>' +
#     '</body></html>', 'html', 'utf-8'))
# # msg = MIMEText('hello, send by Python...', 'plain', 'utf-8')
# #附件
# with open('code.jpg', 'rb') as f:
#     mime = MIMEBase('image', 'jpeg', filename='code.jpg')
#     mime.add_header('Content-Disposition', 'attachment', filename='code.jpg')
#     mime.add_header('Content-ID', '<0>')
#     mime.add_header('X-Attachment-Id', '0')
#     mime.set_payload(f.read())
#     encoders.encode_base64(mime)
#     msg.attach(mime)
# msg['From'] = _format_addr('python customer<%s>' % from_addr)
# msg['To'] = _format_addr('admin <%s>' % to_addr)
# msg['Subject'] = Header('from ....', 'utf-8').encode()
#
# server = smtplib.SMTP(smtp_server, 25)
# server.set_debuglevel(1)
# server.login(from_addr, password)
# server.sendmail(from_addr, [to_addr], msg.as_string())
# server.quit()






