from flask import Flask 
from services.news_fetcher import get_news
from services.summarizer import make_summary
from services.email_sender import send_email

app = Flask(__name__)
@app.route('/')

def home():
    return "Agent is running!"

@app.route('/run')
def trigger():
    try:
        news = get_news()
        summary = make_summary(news)
        send_email(summary)
        return f"<pre>{summary}</pre><br><br><h3>Upar wala copy karke WhatsApp Channel par paste kar do!</h3>"
    except Exception as e:
        return f"error: {e}"

if __name__=='__main__':
    app.run(host='0.0.0.0', port=10000 )