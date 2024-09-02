"""
This module contains a Flask server that serves as an emotion detector.

The server provides two routes:
- "/emotionDetector": Accepts a GET request with a parameter "textToAnalyze" and returns the
  emotion scores and the dominant emotion for the given text.
- "/": Returns the index page.

Usage:
1. Start the server by running this script.
2. Access the routes using a web browser or an HTTP client.

Example:
- Accessing "/emotionDetector" with the parameter "textToAnalyze" set to "I am happy" will return
  the emotion scores and the dominant emotion for the given text.

Note:
- This module requires the EmotionDetection module to be imported.
- The EmotionDetection module should be in the same directory as this script.

Author: Ardhika Putra
Date: 03/09/2024
"""

from flask import Flask, render_template, request
from EmotionDetection import emotion_detector

app = Flask(__name__)


@app.route("/emotionDetector")
def detect_emotion():
    """
    Detects the emotion in a given text using an emotion detector.
    Returns:
        str: A formatted string containing the scores for different emotions
        and the dominant emotion.
    Example:
        For the given statement, the system response is 'anger': 0.5, 'disgust': 0.2,
        'fear': 0.1, 'joy': 0.8, 'sadness': 0.3. The dominant emotion is joy.
    """

    text_to_analyze = request.args.get("textToAnalyze")
    response = emotion_detector(text_to_analyze)

    # Check if the response is valid
    if response["dominant_emotion"] is None:
        return "Invalid Text! Please try again!"

    # Extract the emotion scores and the dominant emotion from the response
    # and return them as a formatted string
    anger_score = response["anger"]
    disgust_score = response["disgust"]
    fear_score = response["fear"]
    joy_score = response["joy"]
    sadness_score = response["sadness"]
    dominant = response["dominant_emotion"]
    return (
        f"For the given statement, the system response is: "
        f"'anger': {anger_score}, 'disgust': {disgust_score}, "
        f"'fear': {fear_score}, 'joy': {joy_score}, "
        f"'sadness': {sadness_score}. Dominant emotion: {dominant}"
    )


@app.route("/")
def index_page():
    """
    Renders the index.html template.
    Returns:
        The HTML template.
    """

    return render_template("index.html")


if __name__ == "__main__":
    app.run(port=5000, debug=True)
