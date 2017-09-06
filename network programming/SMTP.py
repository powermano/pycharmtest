#SMTP
from email.mime.text import MIMEText
from email.utils import formataddr
my_sender='m18260625742@163.com'
my_user='894773140@qq.com'
msg = MIMEText('填写邮件内容', 'plain', 'utf-8')
msg['From'] = formataddr(["FromRunoob", my_sender])  # 括号里的对应发件人邮箱昵称、发件人邮箱账号
msg['To'] = formataddr(["FK", my_user])  # 括号里的对应收件人邮箱昵称、收件人邮箱账号
msg['Subject'] = "菜鸟教程发送邮件测试"  # 邮件的主题，也可以说是标题
# msg = MIMEText('hello, send by Python...', 'plain', 'utf-8')
from_addr = input('From: ')
password = input('Password: ')
# 输入收件人地址:
to_addr = input('To: ')
# 输入SMTP服务器地址:
import smtplib
smtp_server = 'smtp.163.com'
smtp_port = 25
server = smtplib.SMTP(smtp_server, smtp_port)
server.starttls()
# 剩下的代码和前面的一模一样:
server.set_debuglevel(1)


# server = smtplib.SMTP(smtp_server, 465) # SMTP协议默认端口是25
# server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()




