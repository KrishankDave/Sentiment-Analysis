"""
Sentiment Analysis Utility Module
Uses TextBlob for sentiment analysis
"""

from textblob import TextBlob


def get_sentiment(text):
    """
    Analyze the sentiment of the given text.
    
    Args:
        text (str): The text to analyze
        
    Returns:
        dict: A dictionary containing:
            - sentiment: 'Positive', 'Negative', or 'Neutral'
            - polarity: float value between -1 (negative) and 1 (positive)
            - emoji: emoji representation of the sentiment
    """
    if not text or not text.strip():
        return {
            'sentiment': 'Neutral',
            'polarity': 0.0,
            'emoji': '😐'
        }
    
    # Create TextBlob object and get polarity
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    
    # Determine sentiment based on polarity
    if polarity > 0.1:
        sentiment = 'Positive'
        emoji = '😊'
    elif polarity < -0.1:
        sentiment = 'Negative'
        emoji = '😠'
    else:
        sentiment = 'Neutral'
        emoji = '😐'
    
    return {
        'sentiment': sentiment,
        'polarity': round(polarity, 3),
        'emoji': emoji
    }

