import requests
import pandas as pd
import os

# Ваш API ключ (получите его на сайте TMDb)
API_KEY = os.getenv('API_KEY')
TOKEN = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIxMDIzNDExNzVhZDBjYmM3NTNlZGI5NTJhMTA1ZDY1NSIsIm5iZiI6MTczNDEwODU5Mi4wMjcsInN1YiI6IjY3NWM2NWIwMDJhM2QzMzBjNWVlNzVjZiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.HHgIYWareuoa8stXFNvvOmH4fmgHN1cY47d3Sugx4Ug"

# Функция для получения отзывов о фильмах
def get_movie_reviews(movie_id, language='en'):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}/reviews"
    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {TOKEN}"
    }
    params = {
        'api_key': API_KEY,
        'language': language,
        'page': 1
    }
    
    try:
        print(f"Requesting URL: {url}")  # Отладочное сообщение
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()  # Проверка на ошибки HTTP
        reviews = response.json().get('results', [])
        
        review_texts = []
        for review in reviews:
            review_texts.append(review['content'])
        
        return review_texts
    except requests.exceptions.RequestException as e:
        print(f"Error occurred while fetching reviews: {e}")
        return []

# Пример получения отзывов о фильме
movie_id = 550  # Пример: фильм "Бойцовский клуб"
reviews = get_movie_reviews(movie_id)

# Преобразуем в DataFrame и сохраняем в файл
if reviews:
    reviews_df = pd.DataFrame(reviews, columns=['Review'])
    reviews_df.to_csv('data/movie_reviews.csv', index=False)
    print(f"Collected {len(reviews)} reviews for movie {movie_id}")
else:
    print("No reviews collected.")