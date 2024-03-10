import streamlit as st
import google.generativeai as genai
from IPython.display import Markdown
import textwrap
import random

genai.configure(api_key='AIzaSyDlBFVsmV8pao6Ax-bcR0dc5h4CusiNCsc')

def to_markdown(text):
    return text


def prompt(movie_name):
    prompt_parts = [
        f"'As a seasoned movie critic with a broad spectrum of cinematic exposure across languages,"
        f"recommend five movies similar to the given movie-Movie name: {movie_name},"
        f"Also for each movie explain why you find it similar to the given movie and add --- before recommending the next movie'",
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
        recommendations = response.split('---') 
        st.write("Recommendations and Why you'd like them")
        for i, recommendation in enumerate(recommendations, start=1):
            text_color = '#000000'
            background_color = '#' + '%06x' % random.randint(0, 0xFFFFFF) 
            style = f"color: {text_color}; background-color: {background_color}; padding: 10px; border-radius: 15px; margin-bottom: 45px;"
            recommendation_text = recommendation.replace('**', '<strong>', 1).replace('**', '</strong>', 1)
            st.markdown(f"<div style='{style}'>{recommendation_text}</div>", unsafe_allow_html=True)
if __name__ == '__main__':
    main()

