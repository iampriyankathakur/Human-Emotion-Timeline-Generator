import pandas as pd

def compute_trends(df):

    mapping = {
        "Positive": 1,
        "Neutral": 0,
        "Negative": -1
    }

    df["emotion_score"] = df["emotion"].map(mapping)

    return df
