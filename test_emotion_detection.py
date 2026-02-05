from EmotionDetection import emotion_detector

def test_emotion_detection():
    # Joy
    result = emotion_detector("I am glad that this happened")
    assert result["dominant_emotion"] == "joy"

    # Anger
    result = emotion_detector("I am really angry about this")
    assert result["dominant_emotion"] == "anger"

    # Disgust
    result = emotion_detector("I feel disgusted just hearing about this")
    assert result["dominant_emotion"] == "disgust"

    # Sadness
    result = emotion_detector("I am very sad about this")
    assert result["dominant_emotion"] == "sadness"

    # Fear
    result = emotion_detector("I am really afraid that this will happen")
    assert result["dominant_emotion"] == "fear"

    print("All tests passed successfully!")


test_emotion_detection()
