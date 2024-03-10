import streamlit as st
import google.generativeai as genai
from IPython.display import Markdown
import textwrap

genai.configure(api_key='AIzaSyDlBFVsmV8pao6Ax-bcR0dc5h4CusiNCsc')

def prompt(movie_name):
    prompt_parts = [
        f"'As a seasoned movie critic with a broad spectrum of cinematic exposure across languages,"
        f"recommend five movies similar to the given movie-Movie name: {movie_name},"
        f"Also for each movie explain why you find it similar to the given movie'",
    ]
    return prompt_parts
def to_markdown(text):
    text = text.replace('•', '  *')
    return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))
  
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
        st.markdown(to_markdown(response))
if __name__ == '__main__':
    main()

