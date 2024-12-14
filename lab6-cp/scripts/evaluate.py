import pandas as pd
from sklearn.metrics import accuracy_score, classification_report

   # Загрузка результатов анализа тональности
results_df = pd.read_csv('data/sentiment_analysis_results.csv')

# Загрузка истинных меток (замените на ваш файл с метками)
true_labels = [...]  # Замените на ваши истинные метки

   # Получение предсказанных меток
predicted_labels = results_df['Sentiment_Score'].apply(lambda x: 1 if x > 0 else 0)  # Пример: 1 для положительных, 0 для отрицательных

   # Проверка длины массивов
if len(true_labels) != len(predicted_labels):
   print(f"Length of true_labels: {len(true_labels)}, Length of predicted_labels: {len(predicted_labels)}")
else:
       # Оценка модели
    accuracy = accuracy_score(true_labels, predicted_labels)
    print(f'Accuracy: {accuracy:.2f}')

       # Дополнительная информация
    print(classification_report(true_labels, predicted_labels))