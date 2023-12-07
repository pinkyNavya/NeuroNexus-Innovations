import numpy as np
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity


data = {
    'navya': [5, 4, 0, 0, 2],
    'ramu': [0, 5, 4, 0, 1],
    'sita': [2, 0, 5, 4, 0],
    'gopika': [0, 2, 0, 5, 4],
    'krishna': [4, 0, 3, 0, 5],
}

movies = ['Bahubali', 'OMG', 'Mission Majnu', 'Mission Mangal', 'Animal']

df = pd.DataFrame(data, index=movies)

def cosine_similarity_users(user1, user2):
    return cosine_similarity([user1], [user2])[0, 0]


def get_top_similar_users(user, users, n=2):
    similarities = [(other_user, cosine_similarity_users(users[user], users[other_user]))
                    for other_user in users.columns if other_user != user]
    
    similarities.sort(key=lambda x: x[1], reverse=True)
    
    return similarities[:n]


def make_movie_recommendations(user, users, movies, n=2):
    top_similar_users = get_top_similar_users(user, users, n)
    
    recommendations = {}
    
    for movie in movies:
        if users[user][movie] == 0:  
            numerator, denominator = 0, 0
            
            for similar_user, similarity in top_similar_users:
                if users[similar_user][movie] != 0:
                    numerator += similarity * users[similar_user][movie]
                    denominator += np.abs(similarity)
            
            if denominator != 0:
                recommendations[movie] = numerator / denominator
    
    sorted_recommendations = sorted(recommendations.items(), key=lambda x: x[1], reverse=True)
    
    return sorted_recommendations
user_to_recommend = 'krishna'
movie_recommendations = make_movie_recommendations(user_to_recommend, df, movies)

print(f"Movie recommendations for {user_to_recommend}: {movie_recommendations}")
