import csv
import os
from datetime import datetime, timedelta
import pandas as pd
import plotly.express as px
from collections import Counter

LOG_FILE = "mood_log.csv"

mood_score_map = {
    "😊 Happy": 2,
    "🤩 Excited": 2,
    "😌 Calm": 1,
    "😰 Stressed": -1,
    "😢 Sad": -1,
    "😠 Angry": -2
}

def save_log(date, mood, song, quote):
    file_exists = os.path.isfile(LOG_FILE)
    with open(LOG_FILE, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=["date", "mood", "song", "quote"])
        if not file_exists:
            writer.writeheader()
        writer.writerow({
            "date": date,
            "mood": mood,
            "song": song,
            "quote": quote
        })

def load_logs():
    if os.path.exists(LOG_FILE):
        return pd.read_csv(LOG_FILE, parse_dates=["date"])
    else:
        return pd.DataFrame(columns=["date", "mood", "song", "quote"])

def plot_mood_trend(df):
    one_week_ago = datetime.now() - timedelta(days=7)
    df_week = df[df["date"] >= one_week_ago]

    if df_week.empty:
        return px.bar(title="No data to display")

    # Count moods
    mood_counts = df_week["mood"].value_counts().reset_index()
    mood_counts.columns = ["mood", "count"]

    # Score trend
    df_week["score"] = df_week["mood"].map(mood_score_map)
    avg_score = df_week["score"].mean()

    fig = px.bar(
        mood_counts,
        x="mood",
        y="count",
        color="mood",
        color_discrete_sequence=px.colors.qualitative.Safe,
        title="Mood Trend Over the Past 7 Days",
        labels={"count": "Frequency"},
    )

    fig.add_hline(y=avg_score, line_dash="dot", line_color="red", 
                  annotation_text=f"Avg Mood Score: {avg_score:.2f}", 
                  annotation_position="top right")

    return fig
