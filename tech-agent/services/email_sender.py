import smtplib
import html
from pathlib import Path
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from config import config

def send_email(summary):
    """Summary ko Email par bhejta hai"""
    sender = config.MY_EMAIL
    password = config.GMAIL_PASSWORD
    missing_settings = [
        name
        for name, value in (
            ("MY_EMAIL", sender),
            ("GMAIL_PASSWORD", password),
        )
        if not value
    ]
    if missing_settings:
        raise RuntimeError(
            f"Missing email settings in the root .env file: {', '.join(missing_settings)}."
        )

    msg = MIMEMultipart()
    msg['Subject'] = "🚀 Weekly Tech Update"
    msg['From'] = sender
    msg['To'] = sender  # Testing ke liye khud ko, baad me doston ke email daal dena
    template_path = Path(__file__).resolve().parents[1] / "Email_templates" / "email.html"
    if template_path.is_file():
        html_template = template_path.read_text(encoding="utf-8")
        body = html_template.replace(
            "{{summary}}", html.escape(summary).replace("\n", "<br>")
        )
        body = body.replace(
            "{{whatsapp_link}}", html.escape(config.WHATSAPP_CHANNEL_LINK, quote=True)
        )
        msg.attach(MIMEText(body, 'html'))
    else:
        msg.attach(MIMEText(summary, 'plain'))

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
        server.login(sender, password.strip().replace(" ", ""))
        server.send_message(msg)

    print("Email bhej diya!")
    return True