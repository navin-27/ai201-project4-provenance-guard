import os
import json
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)


def analyze_text(text):

    prompt = f"""
You are an AI writing detector.

Analyze the following text.

Return ONLY valid JSON.

Format:

{{
    "attribution":"Likely AI",
    "confidence":0.82
}}

OR

{{
    "attribution":"Likely Human",
    "confidence":0.91
}}

Text:

{text}
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        temperature=0,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    content = response.choices[0].message.content.strip()

    return json.loads(content)