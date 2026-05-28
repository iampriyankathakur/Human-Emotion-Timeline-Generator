import pandas as pd

from src.text_cleaner import clean_text
from src.emotion_detector import detect_emotion
from src.theme_extractor import extract_themes
from src.trend_analyzer import compute_trends
from src.visualizer import plot_emotion_timeline

def main():

    print("\n📖 Human Emotion Timeline Generator\n")

    df = pd.read_csv(
        "data/journal_entries.csv"
    )

    df["clean_entry"] = df["entry"].apply(
        clean_text
    )

    emotions = []
    polarities = []

    for text in df["clean_entry"]:

        emotion, polarity = detect_emotion(
            text
        )

        emotions.append(emotion)
        polarities.append(polarity)

    df["emotion"] = emotions
    df["polarity"] = polarities

    themes = extract_themes(
        df["clean_entry"].tolist()
    )

    df = compute_trends(df)

    print("\nDetected Themes:\n")

    for theme in themes:
        print("-", theme)

    print("\nEmotion Analysis:\n")

    print(df[
        ["date", "emotion", "polarity"]
    ])

    plot_emotion_timeline(df)

if __name__ == "__main__":
    main()
