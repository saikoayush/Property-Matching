import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split

# Load your data
user_df = pd.read_csv('path/to/user_data.csv')
property_df = pd.read_csv('path/to/property_data.csv')

def train_model(user_df, property_df):
    X = user_df
    y = property_df['match_score']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = RandomForestRegressor(n_estimators=100)
    model.fit(X_train, y_train)
    
    return model

if __name__ == "__main__":
    model = train_model(user_df, property_df)
    print("Model Training Complete!")
