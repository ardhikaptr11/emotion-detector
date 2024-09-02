"""
Module: emotion_detection.py

This module includes a function designed to analyze the emotional content of a given text
using the Watson Emotion Detection service.

Functions:
    - emotion_detector(text_to_analyze): Evaluates the emotion present in the provided text
    by leveraging the Watson Emotion Detection service.
"""

import json

import requests


def emotion_detector(text_to_analyze):
    """
    Analyzes the emotion of a given text using the Watson Emotion Detection service.
    Args:
        text_to_analyze (str): The text to be analyzed for emotion detection.
    Returns:
        dict: A dictionary containing the emotion scores and the dominant emotion.
    Raises:
        requests.exceptions.Timeout: If the API request times out.
    Example:
        >>> emotion_detector("I am feeling happy today.")
        {
            'anger': 0.0,
            'disgust': 0.0,
            'fear': 0.0,
            'joy': 0.9,
            'sadness': 0.1,
            'dominant_emotion': 'joy'
        }
    """

    # URL of the emotion detection service
    runtime = "watson.runtime.nlp.v1"
    service = "EmotionPredict"
    url = f"https://sn-watson-emotion.labs.skills.network/v1/{runtime}/NlpService/{service}"
    # Set the headers required for the API request
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    # Create a dictionary with the text to be analyzed
    my_obj = {"raw_document": {"text": text_to_analyze}}
    # Send a POST request to the API with the text and headers
    response = requests.post(url, json=my_obj, headers=header, timeout=5)
    # Format the response text as a JSON object
    formatted_response = json.loads(response.text)
    # Extract the emotion and score from the formatted response
    scores = formatted_response["emotionPredictions"][0]["emotion"]
    # Determine the dominant emotion based on the highest
    dominant = max(scores, key=scores.get)
    # Add the dominant emotion to the scores dictionary
    scores["dominant_emotion"] = dominant

    return scores
