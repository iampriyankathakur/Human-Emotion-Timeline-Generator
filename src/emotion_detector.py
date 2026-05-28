from textblob import TextBlob

def detect_emotion(text):

    polarity = TextBlob(text).sentiment.polarity

    if polarity > 0.2:
        return "Positive", polarity

    if polarity < -0.2:
        return "Negative", polarity

    return "Neutral", polarity
