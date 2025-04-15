import nltk
nltk.download('vader_lexicon')
from nltk.sentiment.vader import SentimentIntensityAnalyzer

def get_sentiment(text):
    sia = SentimentIntensityAnalyzer()
    score = sia.polarity_scores(text)
    compound = score['compound']
    if compound >= 0.5:
        return "😊 Happy"
    elif compound >= 0:
        return "😌 Calm"
    elif compound <= -0.5:
        return "😠 Angry"
    else:
        return "😰 Stressed"
