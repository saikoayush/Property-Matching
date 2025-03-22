import streamlit as st
import pandas as pd
from match_score import calculate_match_score

st.title("Property Matching System")

user_file = st.file_uploader("Upload User Preferences CSV")
property_file = st.file_uploader("Upload Property Data CSV")

if user_file and property_file:
    try:
        # Try reading with UTF-8 encoding
        user_df = pd.read_csv(user_file, encoding="utf-8")
        property_df = pd.read_csv(property_file, encoding="utf-8")
    except UnicodeDecodeError:
        # If UTF-8 fails, try ISO-8859-1 (common for Windows-generated CSVs)
        user_df = pd.read_csv(user_file, encoding="ISO-8859-1")
        property_df = pd.read_csv(property_file, encoding="ISO-8859-1")

    match_scores = calculate_match_score(user_df, property_df)

    st.write("Match Scores:")
    st.dataframe(pd.DataFrame(match_scores))
