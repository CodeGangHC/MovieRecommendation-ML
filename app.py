import pickle
import streamlit as st
from tmdbv3api import Movie, TMDb

movie = Movie()
tmdb = TMDb()
tmdb.api_key = 'efc77c0444049f0ef9d732b9caaf7e1f'

def get_recommendations(title):
    # return index value of a movie based on whole data through a movie title
    idx = movies[movies['title'] == title].index[0]

    # return data according to idx in similarity from cosine similarity matrix (cosine_sim)
    sim_scores = list(enumerate(cosine_sim[idx]))

    # decreasing order based on Cosine similarity
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    # top 10 movies except itself by cosine similarity
    sim_scores = sim_scores[1:11]

    # Get 10 index info of recommended movie list
    movie_indices = [i[0] for i in sim_scores]

    # Get movie title from index info
    images = []
    titles = []
    for i in movie_indices:
        id = movies['id'].iloc[i]
        details = movie.details(id)

        image_path = details['poster_path']
        if image_path:
            image_path = 'https://images.tmdb.org/t/p/w500' + image_path
        else:
            image_path = 'no_image.jpg'

        images.append(image_path)
        titles.append(details['title'])

    return images, titles


movies = pickle.load(open('movies.pickle', 'rb'))
cosine_sim = pickle.load(open('cosine_sim.pickle', 'rb'))

st.set_page_config(layout='wide')
st.header('Chris\' Movie Recommendation')

movie_list = movies['title'].values
title = st.selectbox('Choose a movie you liked!', movie_list)
if st.button('Recommend'):
    with st.spinner('Please wait...'):
        images, titles = get_recommendations(title)

        idx = 0
        for i in range(0, 2):
            cols = st.columns(5)
            for col in cols:
                col.image(images[idx])
                col.write(titles[idx])
                idx += 1
