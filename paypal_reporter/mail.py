import smtplib
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.header import Header

# 接收标题 文件地址
def send_mail(subject, *args):
    sender = '1584436652@qq.com'  # 发送者邮箱
    senderName = "chen"  # 发送者昵称
    password = 'ewwqgccgzkbagiid'  # 发送方QQ邮箱授权码
    mail = '1584436652@qq.com'    # 接收者邮箱
    receivers = [mail]  # 接收邮件
    message = MIMEMultipart()
    message['From'] = Header(senderName, 'utf-8')  # 发送者昵称
    message['Subject'] = Header(subject, 'utf-8')  # 主题
    for content in args:
        with open(content, 'rb') as fp:
            data = fp.read()
        result = MIMEApplication(data)
        # 注意：此处basename要转换为gbk编码，否则中文会有乱码。
        result.add_header('Content-Disposition', 'attachment', filename=('gbk', '',  content))
        message.attach(result)
    try:
        client = smtplib.SMTP_SSL('smtp.qq.com', smtplib.SMTP_SSL_PORT)
        print("连接到邮件服务器成功")
        client.login(sender, password)
        print("登录成功")
        client.sendmail(sender, receivers, message.as_string())
        print("邮件发送成功")
    except smtplib.SMTPException:
        print("Error: 无法发送邮件")



