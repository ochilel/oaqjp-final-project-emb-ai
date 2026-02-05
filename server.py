"""
Flask web server for the Emotion Detection application.

This server exposes an endpoint to analyze emotions from a given text
using the EmotionDetection package.
"""

from flask import Flask, render_template, request
from EmotionDetection import emotion_detector

app = Flask(__name__)


@app.route("/")
def index():
    """
    Render the home page.

    Returns:
        HTML template for the index page.
    """
    return render_template("index.html")


@app.route("/emotionDetector")
def emotion_detector_route():
    """
    Analyze the emotion of the provided text.

    Returns:
        A formatted string with emotion scores and dominant emotion,
        or an error message if the input text is invalid.
    """
    text_to_analyze = request.args.get("text")

    result = emotion_detector(text_to_analyze)

    if result["dominant_emotion"] is None:
        return "¡Texto inválido! ¡Por favor, inténtalo de nuevo!"

    response_text = (
        f"For the given statement, the system response is "
        f"'anger': {result['anger']}, "
        f"'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, "
        f"'joy': {result['joy']} and "
        f"'sadness': {result['sadness']}. "
        f"The dominant emotion is {result['dominant_emotion']}."
    )

    return response_text


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
