"""
Simple test script to demonstrate sentiment analysis functionality
Run this after starting the Django server
"""

import os
import django

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sentiment_app.settings')
django.setup()

from analyzer.utils import get_sentiment

# Test cases
test_texts = [
    "I absolutely love this product! It's amazing and wonderful!",
    "This is the worst experience ever. Terrible and disappointing.",
    "It's okay, nothing special.",
    "The weather is beautiful today!",
    "I hate waiting in long queues.",
    "The service was decent, not great but not bad either.",
    "Fantastic! Best purchase I've ever made!",
    "Horrible quality, waste of money.",
    "The movie was alright.",
    "I'm so happy and excited about this opportunity!"
]

print("=" * 70)
print("REAL-TIME SENTIMENT ANALYZER - TEST RESULTS")
print("=" * 70)
print()

for i, text in enumerate(test_texts, 1):
    result = get_sentiment(text)
    
    print(f"Test {i}:")
    print(f"  Text: {text}")
    print(f"  Sentiment: {result['emoji']} {result['sentiment']}")
    print(f"  Polarity: {result['polarity']}")
    print()

print("=" * 70)
print("All tests completed successfully!")
print("=" * 70)

