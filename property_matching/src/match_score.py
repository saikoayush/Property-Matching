import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

def calculate_match_score(user_df, property_df):
    match_scores = cosine_similarity(user_df, property_df)
    return match_scores

if __name__ == "__main__":
    from preprocess import load_data, preprocess_data

    user_df, property_df = load_data("../data/user_preferences.csv", "../data/property_data.csv")
    user_df, property_df = preprocess_data(user_df, property_df)

    scores = calculate_match_score(user_df, property_df)
    print("Match Scores Computed!")
    print(scores)
