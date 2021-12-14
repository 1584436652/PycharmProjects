import smtplib
from email.mime.text import MIMEText
from email.header import Header
from medals import getWinners, getRanking


def sendmail():
    sender = '1584436652@qq.com'  # 发送邮箱
    senderName = "chen"  # 发送者昵称
    password = 'ewwqgccgzkbagiid'  # 发送方QQ邮箱授权码
    mail = input("输入要发送的邮箱：")
    receivers = [mail]  # 接收邮件

    # 三个参数：第一个为文本内容，第二个 plain 设置文本格式，第三个 utf-8 设置编码
    str = getRanking() + getWinners()
    message = MIMEText(str, 'plain', 'utf-8')
    message['From'] = Header(senderName, 'utf-8')  # 发送者昵称

    # 主题
    subject = '东京奥运会金牌排行榜及获奖人员'
    message['Subject'] = Header(subject, 'utf-8')

    try:
        client = smtplib.SMTP_SSL('smtp.qq.com', smtplib.SMTP_SSL_PORT)
        print("连接到邮件服务器成功")

        client.login(sender, password)
        print("登录成功")

        client.sendmail(sender, receivers, message.as_string())
        print("邮件发送成功")
    except smtplib.SMTPException:
        print("Error: 无法发送邮件")

if __name__ == '__main__':
    print("****奖牌数来源于：https://2020.cctv.com/medal_list****")
    while True:
        sendmail()
