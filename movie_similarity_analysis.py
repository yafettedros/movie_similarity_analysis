import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

# Load datasets
movie_cols = ['movie_id', 'title', 'release_date', 'video_release_date', 'IMDb_URL',
              'unknown', 'Action', 'Adventure', 'Animation', 'Children', 'Comedy',
              'Crime', 'Documentary', 'Drama', 'Fantasy', 'Film-Noir', 'Horror',
              'Musical', 'Mystery', 'Romance', 'Sci-Fi', 'Thriller', 'War', 'Western']
movies = pd.read_csv("u.item", sep="|", names=movie_cols, encoding="latin-1", usecols=range(24))
ratings = pd.read_csv("u.data", sep="\t", names=['user_id', 'movie_id', 'rating', 'timestamp'])

# Compute average rating for each movie
movie_avg_rating = ratings.groupby("movie_id")["rating"].mean().reset_index()
movie_avg_rating.columns = ['movie_id', 'avg_rating']

# Merge genre features with average ratings
movie_features = pd.merge(movies, movie_avg_rating, on="movie_id")
feature_cols = movie_cols[5:] + ['avg_rating']
feature_matrix = movie_features[feature_cols]

# Normalize features
scaler = StandardScaler()
scaled_features = scaler.fit_transform(feature_matrix)

# Compute cosine similarity
similarity_matrix = cosine_similarity(scaled_features)

# Mapping from title to index
title_to_index = pd.Series(movie_features.index, index=movie_features['title']).drop_duplicates()

def get_similar_movies(title, top_n=10):
    index = title_to_index[title]
    similarity_scores = list(enumerate(similarity_matrix[index]))
    similarity_scores = sorted(similarity_scores, key=lambda x: x[1], reverse=True)[1:top_n+1]
    similar_movies = [(movie_features.iloc[i]['title'], round(score, 2)) for i, score in similarity_scores]
    return similar_movies

# Define query movies
queries = ["Star Wars (1977)", "Toy Story (1995)", "Titanic (1997)"]

# Plotting function
def plot_clean_chart(similar_movies, title, color):
    titles = [movie[0] for movie in similar_movies]
    scores = [movie[1] for movie in similar_movies]

    plt.figure(figsize=(10, 6))
    bars = plt.bar(titles, scores, color=color)
    plt.xticks(rotation=45, ha='right')
    plt.ylabel('Similarity Score')
    plt.title(f'Top 10 Similar Movies to {title}')
    plt.ylim(0.85, 1.0)
    plt.gca().spines['top'].set_visible(False)
    plt.gca().spines['right'].set_visible(False)
    plt.gca().spines['left'].set_visible(False)
    plt.gca().spines['bottom'].set_visible(False)
    plt.tick_params(left=False, bottom=False)
    plt.grid(False)

    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2.0, yval + 0.005, f"{yval:.2f}", ha='center', va='bottom')

    plt.tight_layout()
    plt.show()

# Run for each query
colors = ["#4c72b0", "#dd8452", "#55a868"]
for i, query in enumerate(queries):
    print(f"\nTop 10 movies similar to '{query}':")
    similar = get_similar_movies(query)
    for rank, (title, score) in enumerate(similar, 1):
        print(f"{rank}. {title} - {score}")
    plot_clean_chart(similar, query, color=colors[i])
