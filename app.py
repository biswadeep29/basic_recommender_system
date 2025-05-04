import streamlit as st
import pickle
import pandas as pd
import requests

movies_dict = pickle.load(open('movie_dict.pkl','rb'))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open('similarity.pkl','rb'))

def fetch_poster(movie_id):
    url =  "https://api.themoviedb.org/3/movie/{}?api_key=9ab59f8a2f3f38d90b2e1b62634f0a18&language=en-US".format(movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/"+poster_path
    return full_path

def recommend(movie_name):
    movie_index = movies[movies['title'] == movie_name].index[0]
    dists = similarity[movie_index]
    movie_list = sorted(list(enumerate(dists)),reverse=True,key=lambda x : x[1])[1:4]

    recommended_movies = []
    recommended_movie_posters = []

    for i in movie_list:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        # fetch poster from api
        recommended_movie_posters.append(fetch_poster(movie_id))

    return recommended_movies,recommended_movie_posters

st.title("Movie Recommender System")

selected_movie_name = st.selectbox(
    "Similar movies to ?",
    movies['title'].values
)

if st.button('Recommend'):
    recommendations,posters = recommend(selected_movie_name)
    col1, col2, col3 = st.columns(3)
    with col1:
        st.text(recommendations[0])
        st.image(posters[0])
    with col2:
        st.text(recommendations[1])
        st.image(posters[1])

    with col3:
        st.text(recommendations[2])
        st.image(posters[2])