from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import pandas as pd

# Инициализируем анализатор VADER
analyzer = SentimentIntensityAnalyzer()

# Загружаем предобработанные данные
reviews_df = pd.read_csv('data/processed_movie_reviews.csv')

def analyze_sentiment(text):
    sentiment = analyzer.polarity_scores(text)
    return sentiment['compound']

# Применяем анализ тональности
reviews_df['Sentiment_Score'] = reviews_df['Cleaned_Review'].apply(analyze_sentiment)

# Сохраняем результаты
reviews_df.to_csv('data/sentiment_analysis_results.csv', index=False)

print("Sentiment analysis complete. Saved to 'data/sentiment_analysis_results.csv'.")
