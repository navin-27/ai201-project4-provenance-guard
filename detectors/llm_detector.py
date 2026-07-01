import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))


def analyze_text(text):
    prompt = f"""
You are an AI content detector.

Analyze the following text and estimate how likely it is to have been AI-generated.

Return ONLY valid JSON in this exact format:

{{
    "attribution":"Likely AI" or "Likely Human",
    "confidence":0.85
}}

Text:
{text}
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0
    )

    return response.choices[0].message.content