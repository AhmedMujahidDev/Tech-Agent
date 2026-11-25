import os
import google.generativeai as genai
from config import config

MODEL_NAME = os.environ.get("GEMINI_MODEL", "gemini-3.6-flash")

def make_summary(news):
    """Convert news into Urdu and English."""
    if not config.GEMINI_KEY:
        raise RuntimeError("GEMINI_KEY is missing; add it to the root .env file.")

    genai.configure(api_key=config.GEMINI_KEY)
    model = genai.GenerativeModel(MODEL_NAME)

    prompt = f"""
    Is Tech News ko aasan Urdu + English mix me summarize karo.
    Aise likho jaise koi dost bata raha ho.

    Is format me likho:
    🚀 WEEKLY TECH UPDATE

    1. Tech Market Me Kya Chal Raha Hai?
    2. Frontend / React / Angular Me Kya Naya Hai?
    3. AI Me Kya Naya Hai?
    4. Agle Hafte Kya Hone Wala Hai?

    Aakhir me ek line likho: "Is hafte ka sabse bada lesson kya hai?"

    News:
    {news}
    """

    response = model.generate_content(prompt)
    if not response.text:
        raise RuntimeError("The Gemini API returned an empty summary.")
    return response.text