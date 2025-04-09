import streamlit as st
from datetime import datetime
from suggestions import get_suggestion
from mood_utils import save_log, load_logs, plot_mood_trend

st.set_page_config(page_title="Mood-Based Music Journal", layout="centered")

st.title("🌈 Mood-Based Music Journal")
st.subheader("Track how you feel and get personalized motivation 🎵")

emoji_moods = {
    "😊 Happy": "😊 Happy",
    "😢 Sad": "😢 Sad",
    "😠 Angry": "😠 Angry",
    "😌 Calm": "😌 Calm",
    "😰 Stressed": "😰 Stressed",
    "🤩 Excited": "🤩 Excited"
}

# Mood Input
mood = st.radio("How are you feeling today?", list(emoji_moods.keys()), horizontal=True)

if st.button("Log Mood 🎯"):
    date = datetime.now().strftime("%Y-%m-%d")
    song, quote = get_suggestion(mood)

    save_log(date, mood, song, quote)

    st.success("Mood logged successfully!")
    st.markdown(f"**🎵 Suggested Song:** {song}")
    st.markdown(f"**💬 Quote:** {quote}")

st.divider()

# Logs + Chart
df_logs = load_logs()

if not df_logs.empty:
    st.subheader("📊 Mood Trend (Last 7 Days)")
    fig = plot_mood_trend(df_logs)
    st.plotly_chart(fig, use_container_width=True)

    st.subheader("🧾 Mood Log History")
    st.dataframe(df_logs[::-1], use_container_width=True)
else:
    st.info("No mood logs yet. Start by logging your mood above!")
