# MovieRecommendation-ML<br>
First Machine Learning Project.<br>
Used Python and Jupyter Notebook to create a Movie Recommendation System.<br>
This ML model is trained based on movie contents and will recommend movies based on similar contents: genre, director, keywords, etc.<br>
Data were collected through kaggle:
https://www.kaggle.com/code/ibtesama/getting-started-with-a-movie-recommendation-system
I've created a soup that contains cast, director, keywords, genres.<br>
And then calculated cosine similarity to compare the movies, so that later on the model can suggest the movie based on higher cosine similarity.<br>
I dumped the movie info to movies.pickle and cosine similarity to cosine_sim.pickle.<br> 
(cosine similarty File was too big and was unable to attach. Please reference the 'Movie Recommendation System.ipynb' for details of what I've done.<br>
Way it runs is simple. Run it on virtual environment and run it through Streamlit:
![example5](https://github.com/CodeGangHC/MovieRecommendation-ML/assets/104274844/08b89246-82cd-459e-90ae-f94d7d439301)
First Screen pops up:
![example1](https://github.com/CodeGangHC/MovieRecommendation-ML/assets/104274844/26791564-b143-4e39-8b15-423ac68efed7)
You can click on movie title to see the list and select one you liked.
![example2](https://github.com/CodeGangHC/MovieRecommendation-ML/assets/104274844/8176ff21-0536-4c37-953f-c9905ab6f71a)
Or even you can type it if you know your movie title.
![example2-1](https://github.com/CodeGangHC/MovieRecommendation-ML/assets/104274844/4683e673-e851-47a7-b387-77790e27ade4)
When you click 'Recommend' button, it'll show a loading bar until the movies load.
![example3](https://github.com/CodeGangHC/MovieRecommendation-ML/assets/104274844/68f0a9d0-024b-41b4-862f-9d09afc4dda7)
It'll show up to 10 movies that are similar to the one you picked.
![example4](https://github.com/CodeGangHC/MovieRecommendation-ML/assets/104274844/ceb5705c-4dd7-45a5-876b-cc2b7aaa544c)
