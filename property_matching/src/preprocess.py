import pandas as pd
import re

def clean_price(value):
    """Convert price strings like '$500k' or '$1.2M' to numeric values."""
    if isinstance(value, str):
        value = value.replace("$", "").replace(",", "").strip().lower()
        if "k" in value:
            return float(value.replace("k", "")) * 1000
        elif "m" in value:
            return float(value.replace("m", "")) * 1000000
        else:
            return float(value)  # Normal number
    return value  # If already numeric, return as is

def preprocess_data(user_df, property_df):
    """Clean and preprocess data for matching."""
    
    # Convert price column (Modify column name based on your dataset)
    if "budget" in user_df.columns:
        user_df["budget"] = user_df["budget"].apply(clean_price)
    
    if "price" in property_df.columns:
        property_df["price"] = property_df["price"].apply(clean_price)

    return user_df, property_df
