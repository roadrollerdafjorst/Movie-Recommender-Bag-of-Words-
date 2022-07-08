import streamlit as st
import pandas as pd
import pickle
import requests

st.title('Movies Recommender')

movies_list = pickle.load(open('venv/movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_list)


def fetch_poster(movie_id):
    response = requests.get(
        f'https://api.themoviedb.org/3/movie/{movie_id}?api_key=8ca76b2d60707532efa33c015ac28182&language=en-US')
    data = response.json()
    return "https://image.tmdb.org/t/p/original" + data['poster_path']


def recommend_movie(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    top_ten = sorted(list(enumerate(distances)), key=lambda x: x[1], reverse=True)[1:11]
    recommend_movies = []
    recommend_posters = []
    for i in top_ten:
        recommend_movies.append(movies.iloc[i[0]]['title'])
        recommend_posters.append(fetch_poster(movies.iloc[i[0]]['movie_id']))
    return recommend_movies, recommend_posters


selected_movie = st.selectbox(
    'Enter Movie Name',
    movies['title'].values)

similarity = pickle.load(open('venv/similarity.pkl', 'rb'))

if st.button('Recommend'):
    rec, posters = recommend_movie(selected_movie)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(rec[0])
        st.image(posters[0])
    with col2:
        st.text(rec[1])
        st.image(posters[1])
    with col3:
        st.text(rec[2])
        st.image(posters[2])
    with col4:
        st.text(rec[3])
        st.image(posters[3])
    with col5:
        st.text(rec[4])
        st.image(posters[4])
