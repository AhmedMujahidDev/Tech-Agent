import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from config import config

def send_email(summary):
    """Summary ko Email par bhejta hai"""
    sender = Config.MY_EMAIL
    password = Config.GMAIL_PASSWORD

    msg = MIMEMultipart()
    msg['Subject'] = "🚀 Weekly Tech Update"
    msg['From'] = sender
    msg['To'] = sender  # Testing ke liye khud ko, baad me doston ke email daal dena
     # HTML Email banane ke liye template use karo
    try:
        with open("templates/email.html", "r", encoding="utf-8") as f:
            html_template = f.read()
        body = html_template.replace("{{summary}}", summary.replace("\n", "<br>"))
        body = body.replace("{{whatsapp_link}}", Config.WHATSAPP_CHANNEL_LINK)
        msg.attach(MIMEText(body, 'html'))
    except:
        # Agar template na mile to simple text bhej do
        msg.attach(MIMEText(summary, 'plain'))

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
        server.login(sender, password)
        server.send_message(msg)

    print("Email bhej diya!")
    return True