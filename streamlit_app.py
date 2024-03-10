import streamlit as st
import google.generativeai as genai
from IPython.display import Markdown
import textwrap

genai.configure(api_key='AIzaSyDlBFVsmV8pao6Ax-bcR0dc5h4CusiNCsc')

def to_markdown(text):
    return text


def prompt(movie_name):
    prompt_parts = [
        f"'As a seasoned movie critic with a broad spectrum of cinematic exposure across languages,"
        f"recommend five movies similar to the given movie-Movie name: {movie_name},"
        f"Also for each movie explain why you find it similar to the given movie .After each movie recommendation in the 5 add 3 newlines'",
    ]
    return prompt_parts
    
def recommend(movie_name, model):
    human_prompt = prompt(movie_name)
    response = model.generate_content(human_prompt)
    return response.text
def main():
    st.title('Movie Recommendation App')
    movie_name = st.text_input('Enter the movie name:')
    if movie_name:
        model = genai.GenerativeModel(model_name="gemini-pro")
        response = recommend(movie_name, model)
        recommendations = response.split('\n\n\n') 
        for i, recommendation in enumerate(recommendations, start=1):
            text_color = '#FFFFFF'
            background_color = '#4E342E' if i % 2 == 0 else '#795548'
            style = f"color: {text_color}; background-color: {background_color}; padding: 10px; border-radius: 15px; margin-bottom: 50px;"
            st.markdown(f"<div style='{style}'>{recommendation}</div>", unsafe_allow_html=True)
if __name__ == '__main__':
    main()

