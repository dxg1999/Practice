# coding： utf-8

# @Author: Duanxiaogang
# @File :SendMail.py
# @DATE :2022/11/29
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
from conf import settings
from common.feishuapi import feishu
from conf.logger import Logger

log = Logger(logger="log_msg").getlogger()


def send_email(report_file):
    msg = MIMEMultipart()

    fei = feishu()

    msg['From'] = '986099850@qq.com'
    msg['To'] = '收件人'
    msg['Subject'] = Header(settings.subject, 'utf-8')  # 从配置文件中读取

    mail_msg = '领导好，附件为测试报告，您请查收'
    msg.attach(MIMEText(mail_msg, 'plain', 'utf-8'))

    # msg.attach(MIMEText(open(report_file, encoding='utf-8').read(), 'html', 'utf-8'))

    att1 = MIMEText(open(report_file, 'rb').read(), 'html', 'utf-8') # 从配置文件中读取
    att1["Content-Type"] = 'application/octet-stream'
    att1["Content-Disposition"] = 'attachment; filename="{}"'.format(report_file)  # 参数化一下report_file
    msg.attach(att1)

    try:
        smtp = smtplib.SMTP_SSL(settings.smtp_server, 465)  # 从配置文件中读取
        smtp.login(settings.smtp_user, settings.smtp_password)  # 从配置文件中读取
        smtp.sendmail(settings.sender, settings.receiver, msg.as_string())  # 发送另一个邮箱
        log.info("邮件发送完成！")
        fei.send_text_msg('邮件发送完成！')
    except Exception as e:
        log.error('发送失败',e)


if __name__ == '__main__':
    send_email()
