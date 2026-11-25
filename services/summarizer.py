def make_summary(news):
    """convert news into urdu and english """
    genai.configure(api_key=config.GEMINI_KEY)
    model = genai.GenerativeModel("gemini-2.0-flash")

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