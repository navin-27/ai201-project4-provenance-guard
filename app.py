from flask import Flask, request, jsonify
import uuid
import json

from services.audit_log import save_entry, load_log
from detectors.llm_detector import analyze_text

app = Flask(__name__)


@app.route("/")
def home():
    return {
        "message": "Welcome to Provenance Guard API"
    }


@app.route("/submit", methods=["POST"])
def submit():

    data = request.get_json()

    creator_id = data.get("creator_id")
    text = data.get("text")

    content_id = str(uuid.uuid4())

    # Analyze text using Groq
    result = analyze_text(text)

    # Convert JSON string returned by Groq into Python dictionary
    analysis = json.loads(result)

    response = {
        "content_id": content_id,
        "creator_id": creator_id,
        "text": text,
        "attribution": analysis["attribution"],
        "confidence": analysis["confidence"],
        "label": "LLM Analysis Completed"
    }

    save_entry(response)

    return jsonify(response)


@app.route("/log", methods=["GET"])
def get_log():
    return jsonify(load_log())


if __name__ == "__main__":
    app.run(debug=True)