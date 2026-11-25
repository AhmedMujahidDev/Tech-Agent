import feedparser
from config import config

def get_news():
    """colect news from website and convert it in string"""
    news = ""
    for url in config.NEWS_SOURCES:
        try:
            feed= feedparser.parse(url)
            for entry in feed.entries[:5]:
                news +=f"-{entry.title}\n"
        except Exception as e:
            print(f"Error fetching {url}: {e}")
            continue
    if not news.strip():
        raise RuntimeError("No news items were fetched; check your network and feed sources.")
    return news
