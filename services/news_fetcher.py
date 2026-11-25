import feedparser
from config import config

def get_news():
    """colect news from website and convert it in string"""
    news = ""
    for url in config.NEWS_SOURCES:
        try:
            feed= feedparser.parse(url)
            for entery in feed.entries[:5]:
                news +=f"-{entry.title}\n"
        except Exception as e:
            print(f"Error fetching {url}: {e}")
            continue
    return news
