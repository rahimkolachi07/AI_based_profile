import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def email_sending(receiver,text,subject):
    email_content = text
    sender_email = "rahimkolachi16@gmail.com"
    receiver_email = receiver
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject
    msg.attach(MIMEText(email_content, 'plain'))
    smtp_server = 'smtp.gmail.com'
    port = 587 
    username = "rahimkolachi16@gmail.com"
    password = "icsagosxvhnbiudq"
    server = smtplib.SMTP(smtp_server, port)
    server.starttls()
    server.login(username, password)
    server.sendmail(sender_email, receiver_email, msg.as_string())
    server.quit()
