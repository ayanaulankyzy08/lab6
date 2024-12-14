from transformers import pipeline, AutoTokenizer
import pandas as pd

# Загружаем модель Hugging Face для анализа эмоций
emotion_classifier = pipeline("text-classification", model="j-hartmann/emotion-english-distilroberta-base")
tokenizer = AutoTokenizer.from_pretrained("j-hartmann/emotion-english-distilroberta-base")

# Загружаем данные
reviews_df = pd.read_csv('data/processed_movie_reviews.csv')

def classify_emotion(text):
    try:
        # Обрезаем текст до 512 токенов
        if len(text.split()) > 512:
            text = ' '.join(text.split()[:512])
        tokens = tokenizer.encode(text, truncation=True, max_length=512, return_tensors='pt')
        result = emotion_classifier(tokens)
        return result[0]['label']
    except Exception as e:
        print(f"Error processing text: {text[:30]}... - {e}")
        return None  # Или любое другое значение по умолчанию

if __name__ == '__main__':
    # Применяем анализ эмоций
    reviews_df['Emotion'] = reviews_df['Cleaned_Review'].apply(classify_emotion)

    # Сохраняем результаты
    reviews_df.to_csv('data/emotion_analysis_results.csv', index=False)

    print("Emotion analysis complete. Saved to 'data/emotion_analysis_results.csv'.")