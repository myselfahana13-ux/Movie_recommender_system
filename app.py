import streamlit as st
import pandas as pd 
import pickle
import requests


def recommend(movie):
    movie_idx = movies[movies['title']== movie].index[0]
    dist = sim[movie_idx]
    movies_list = sorted(list(enumerate(dist)),reverse=True, key=lambda x:x[1])[1:6]
    
    recommended_movies = []
    for i in movies_list:
        
        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies

    
movies_dict = pickle.load(open('movie_dict.pkl','rb'))
movies = pd.DataFrame(movies_dict)

sim = pickle.load(open('sim.pkl','rb'))

st.title('Movie Recommender System')

selected_movie_name = st.selectbox(
   'Hello' ,movies['title'].values)

if st.button('recommend'):
    recommendations = recommend(selected_movie_name)
    for i in recommendations:
        st.write(i)

    
