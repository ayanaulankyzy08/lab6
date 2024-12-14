import nltk
import spacy
import re
import pandas as pd
from nltk.corpus import stopwords
from spacy.lang.en import English

# Загрузка стоп-слов
nltk.download('stopwords')
stop_words = set(stopwords.words('english'))

# Загрузка spaCy модели
nlp = spacy.load('en_core_web_sm')

def clean_text(text):
    # Убираем все символы, кроме букв и пробелов
    text = re.sub(r'[^a-zA-Z\s]', '', text, re.I)
    text = text.lower()  # Приводим к нижнему регистру
    return text

def tokenize_and_lemmatize(text):
    # Токенизация и лемматизация с использованием spaCy
    doc = nlp(text)
    tokens = [token.lemma_ for token in doc if token.text not in stop_words]
    return tokens

# Загружаем данные
reviews_df = pd.read_csv('data/movie_reviews.csv')

# Применяем очистку и токенизацию
reviews_df['Cleaned_Review'] = reviews_df['Review'].apply(clean_text)
reviews_df['Tokens'] = reviews_df['Cleaned_Review'].apply(tokenize_and_lemmatize)

# Сохраняем предобработанные данные
reviews_df.to_csv('data/processed_movie_reviews.csv', index=False)

print("Preprocessing complete. Saved to 'data/processed_movie_reviews.csv'.")
