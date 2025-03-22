from src.preprocess import load_data, preprocess_data
from src.match_score import calculate_match_score
import pandas as pd

if __name__ == "__main__":
    # Load data
    user_df, property_df = load_data("data/user_preference.csv", "data/property_datas.csv")

    # Preprocess data
    user_df, property_df = preprocess_data(user_df, property_df)

    # Compute Match Scores
    match_scores = calculate_match_score(user_df, property_df)

    # Save results
    match_scores_df = pd.DataFrame(match_scores, 
                                   index=[f"User_{i}" for i in range(len(user_df))],
                                   columns=[f"Property_{j}" for j in range(len(property_df))])

    match_scores_df.to_csv("data/match_scores.csv", index=True)
    print("Final Match Scores:")
    print(match_scores_df)
