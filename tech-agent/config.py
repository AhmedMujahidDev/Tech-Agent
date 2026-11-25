import os
from dotenv import load_dotenv

load_dotenv()

class Config:
     # Gemini AI Key
    GEMINI_KEY = os.environ.get("GEMINI_KEY")

    # Gmail Settings
    MY_EMAIL = os.environ.get("MY_EMAIL")
    GMAIL_PASSWORD = os.environ.get("GMAIL_PASSWORD")

    # WhatsApp Channel Link
    WHATSAPP_CHANNEL_LINK = "Follow the Tech Updates channel on WhatsApp: https://whatsapp.com/channel/0029VbDpW7S6GcGKvuwCxp3z"

    # Sources
NEWS_SOURCES_BY_CATEGORY = {
     "pakistan": [
    "https://propakistani.pk/feed",
    "https://www.techjuice.pk/feed",
    "https://tribune.com.pk/feed/technology",
    "https://www.brecorder.com/feeds/technology",
    "https://www.dawn.com/feeds/home",
     ],

     "global_tech": [
     "https://techcrunch.com/feed/",
     "https://www.theverge.com/rss/index.xml",
     "https://www.wired.com/feed/rss",
     "https://feeds.arstechnica.com/arstechnica/index",
     "https://www.technologyreview.com/feed/",
     "https://venturebeat.com/feed/",
     "https://restofworld.org/feed/",
     ],

     "ai": [
     "https://openai.com/news/rss.xml",
     "https://huggingface.co/blog/feed.xml",
     "https://blog.google/technology/ai/rss/",
     ],

     "security": [
     "https://www.bleepingcomputer.com/feed/",
     "https://krebsonsecurity.com/feed/",
     "https://feeds.feedburner.com/TheHackersNews",
     ],

     "dev": [
     "https://dev.to/feed",
     "https://news.ycombinator.com/rss",
     "https://github.blog/feed/",
     "https://stackoverflow.blog/feed/",
     "https://feed.infoq.com/",
     ],

     "software_engineering": [
     "https://feed.infoq.com/",
     "https://martinfowler.com/feed.atom",
     "https://blog.pragmaticengineer.com/rss/",
     "https://blog.bytebytego.com/feed",
     "https://thenewstack.io/feed/",
     "https://netflixtechblog.com/feed",
     "https://blog.cloudflare.com/rss/",
     "https://aws.amazon.com/blogs/architecture/feed/",
     "https://stackoverflow.blog/feed/",
     "https://github.blog/feed/",
     "https://hnrss.org/best",
     ],

     "data_science": [
     "https://www.kdnuggets.com/feed",
     "https://towardsdatascience.com/feed",
     "https://www.analyticsvidhya.com/feed/",
     "https://machinelearningmastery.com/blog/feed/",
     "https://www.databricks.com/feed",
     "https://developer.nvidia.com/blog/feed/",
     "https://simonwillison.net/atom/everything/",
     "https://magazine.sebastianraschka.com/feed",
     ],

     "research": [
     "https://bair.berkeley.edu/blog/feed.xml",
     "https://research.google/blog/rss/",
     "https://huggingface.co/blog/feed.xml",
     "http://export.arxiv.org/rss/cs.LG",
     "http://export.arxiv.org/rss/stat.ML",
     ],
}

config = Config()
config.NEWS_SOURCES = tuple(
    url
    for sources in NEWS_SOURCES_BY_CATEGORY.values()
    for url in sources
)