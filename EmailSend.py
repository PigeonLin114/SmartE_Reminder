import smtplib
from email.mime.text import MIMEText
from email.header import Header
from JSON_GET import *
def send_simple_email(variable_content, recipient_email, subject="变量内容邮件"):

    # 邮箱配置 - 请修改为你的实际信息
    sender_email = ""
    sender_password = ""  
    smtp_server = ""
    smtp_port = 465 #根据邮件服务器更改

    # 创建邮件内容
    message = MIMEText(f"宿舍剩余的电量是: {variable_content},记得及时充电费喔,", 'plain', 'utf-8')
    message['From'] = Header(sender_email)
    message['To'] = Header(recipient_email, 'utf-8')
    message['Subject'] = Header(subject, 'utf-8')

    try:
        # 发送邮件
        server = smtplib.SMTP_SSL(smtp_server, smtp_port)
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, recipient_email, message.as_string())
        server.quit()
        print("邮件发送成功！")
        return True
    except Exception as e:
        print(f"邮件发送失败: {e}")
        return False


# 使用示例
if __name__ == "__main__":
    # 你的变量内容
    my_variable = odd_value

    # 发送邮件
    send_simple_email(
        variable_content=my_variable,
        recipient_email="",  # 替换为实际收件人
        subject="电量提醒"
    )