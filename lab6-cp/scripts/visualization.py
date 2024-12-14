import streamlit as st
import pandas as pd

# Загружаем результаты анализа
reviews_df = pd.read_csv('data/sentiment_analysis_results.csv')

# Стартовое окно
st.title('Movie Review Sentiment Analysis')

# Выводим первые несколько строк
st.write("Sentiment Analysis Results:")
st.write(reviews_df[['Review', 'Sentiment_Score']].head())

# График
st.bar_chart(reviews_df['Sentiment_Score'])
