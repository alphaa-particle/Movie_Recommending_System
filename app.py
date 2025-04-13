import streamlit as st
import pickle
import pandas as pd
import requests

def fetch_poster(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=cfec5cc060c9f5686c59bf32768f7c68&language=en-US'.format(movie_id))
    data = response.json()
    return 'http://image.tmdb.org/t/p/w500/' + data['poster_path']

def recommend(movie):
    movie_index = movies[movies['title']==movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)),reverse = True, key=lambda x:x[1])[1:6]

    recommended_movies = []
    recommended_movies_posters = []

    for i in movies_list:

        movie_id = movies.iloc[i[0]].movie_id
        # Fetch Poster from the API
        recommended_movies.append(movies.iloc[i[0]].title)
        # Fetch Poster from the API
        recommended_movies_posters.append(fetch_poster(movie_id))

    return recommended_movies,recommended_movies_posters

movies_dict = pickle.load(open('movie_dict.pkl' , 'rb'))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open('similarity.pkl' , 'rb'))

st.title('Movie Recommending System')

selected_movie_name = st.selectbox(
"Enter the movie for which you want the recommendations",
movies['title'].values)

if st.button('Click to Recommend'):
    names,posters = recommend(selected_movie_name)

    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.subheader(names[0])
        st.image(posters[0])

    with col2:
        st.subheader(names[1])
        st.image(posters[1])

    with col3:
        st.subheader(names[2])
        st.image(posters[2])

    with col4:
        st.subheader(names[3])
        st.image(posters[3])

    with col5:
        st.subheader(names[4])
        st.image(posters[4])
