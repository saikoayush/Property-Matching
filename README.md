
------PROJET TITLE---------
# Property Matching with User Preferences

## Description
This project focuses on developing a system that matches properties with user preferences and calculates a **Match Score** for each user-property pair. The system processes provided datasets, applies AI/ML techniques to quantify similarity, and optionally features a UI for real-time match score calculation.

## Features
- **Data Processing**: Cleans and preprocesses datasets (handles missing values, normalizes numerical features, and encodes categorical variables).
- **Match Score Calculation**: Uses AI/ML techniques like similarity metrics, embeddings, or LLMs to assess compatibility between user preferences and property characteristics.
- **Implementation**: Developed using Python with libraries such as Scikit-learn, TensorFlow, PyTorch, or Hugging Face.
- **Presentation & Visualization**: Includes charts and graphs for intuitive representation of Match Scores.
- **Optional UI**: A simple interactive interface built using Streamlit/Flask/Gradio for real-time user-property match scoring.

## Technologies Used
- **Programming Language**: Python
- **Libraries & Frameworks**:
  - Pandas & NumPy (Data Processing)
  - Scikit-learn (Machine Learning)
  - TensorFlow/PyTorch (Deep Learning, if applicable)
  - Matplotlib/Seaborn (Visualization)
  - Streamlit/Flask/Gradio (Optional UI)

## Installation
### Prerequisites
Ensure you have Python installed along with the required libraries. Install dependencies using:
pip install -r requirements.txt


## Usage
1. **Run the Data Processing Script**:
   python data_processing.py

2. **Run the Match Score Calculation**:
  python match_score.py


## Methodology
1. **Data Cleaning & Preprocessing**:
   - Handled missing values.
   - Normalized numerical data.
   - Encoded categorical features.
2. **Match Score Calculation**:
   - Designed a scoring mechanism using similarity metrics, embeddings, or ML models.
   - Justified model selection and fine-tuned parameters.
3. **Implementation**:
   - Used Python-based ML frameworks for computation.
   - Created a presentable output with visualizations.

## Results & Visualizations
- Match Scores are visualized using simple UI.
- Sample user-property matches are demonstrated.

## Confusion
-After matching the files, it gives some error like **ValueError: could not convert string to float: '$500k'**,
but the backend code is running smoothly and give the "Match_score.csv" file also.

## Support
-ayushvashishtha93@gmail.com
-8810509363




