from textblob import TextBlob
def analyze_sentiment(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    if polarity > 0:
        return 'positive'
    elif polarity < 0:
        return 'negative'
    else:
        return 'neutral'
sentences = [
    "I love this product!",
    "It's amazing.",
    "The weather is terrible today."
]
for sentence in sentences:
    sentiment = analyze_sentiment(sentence)
    print(f"Sentence: '{sentence}'")
    print("Sentiment:", sentiment)
    print()
