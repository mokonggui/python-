import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
def sendfun():
    # 邮箱配置
    smtp_server = 'smtp.qq.com'
    smtp_port = 465
    # 发送人QQ邮箱
    sender = '123456@qq.com'
    # smtp授权码
    password = '******'
    # 接收人邮箱
    receiver = '123456789@qq.com'
    # 构造邮件
    msg = MIMEMultipart()
    msg['From'] = sender
    msg['To'] = receiver
    msg['Subject'] = '图片'
    # 遍历文件夹中的所有图片
    for filename in os.listdir('./image'):
        if filename.endswith('.jeg') or filename.endswith('.png'):
            # 读取图片数据
            with open(os.path.join('image', filename), 'rb') as f:
                img_data = f.read()
            # 构造图片附件
            img = MIMEImage(img_data)
            img.add_header('Content-Disposition', 'attachment', filename=filename)
            msg.attach(img)
    # 发送邮件
    try:
        server = smtplib.SMTP_SSL(smtp_server, smtp_port)
        server.login(sender, password)
        server.sendmail(sender, receiver, msg.as_string())
        server.quit()
        print('邮件发送成功')
    except Exception as e:
        print('邮件发送失败:', e)
