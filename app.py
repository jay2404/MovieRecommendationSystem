import streamlit as st
import pickle
import pandas as pd
import requests

def fetch_poster(movie_id):
    requests.get()


def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]


    recommended_movies =[]
    for i in movies_list:
        movie_id =i[0]
        #fetch poster from api
        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies

# here we use padnas to access our pickle file cos we canot open dict file through pickle
movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
#  here we make data frame of movie
movies =pd.DataFrame(movies_dict)
similarity =pickle.load( open('similar_movie.pkl', 'rb'))
st.title('Movie Recommender System')

selected_movie_name = st.selectbox(
    'How would you like to be contacted?',
   movies['title'].values )
if st.button('Recommend'):
    recommendations = recommend(selected_movie_name)
    for i in recommendations:
      st.write(i)