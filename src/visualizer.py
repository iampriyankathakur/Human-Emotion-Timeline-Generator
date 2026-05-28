import matplotlib.pyplot as plt

def plot_emotion_timeline(df):

    plt.figure(figsize=(10,5))

    plt.plot(
        df["date"],
        df["emotion_score"],
        marker="o"
    )

    plt.title("Emotion Timeline")

    plt.xlabel("Date")

    plt.ylabel("Emotion Score")

    plt.grid(True)

    plt.savefig(
        "outputs/emotion_timeline.png"
    )

    plt.show()
