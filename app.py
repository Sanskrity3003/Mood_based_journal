import streamlit as st
from datetime import datetime
from mood_utils import save_log, load_logs, plot_mood_trend
from sentiment_utils import get_sentiment
from suggestions import get_suggestion
from spotify_utils import get_spotify_url
import re

# ---- PAGE CONFIG ----
st.set_page_config(
    page_title="🎶 Mood-Based Journal",
    page_icon="🧠",
    layout="centered"
)

# ---- SIDEBAR ----
st.sidebar.title("📌 Navigation")
page = st.sidebar.radio("Go to", ["Log Mood", "View Insights", "Journal & Sentiment", "About"])

st.sidebar.markdown("---")
st.sidebar.markdown("Created with ❤️ using Streamlit + Plotly + Spotify API")

# ---- COMMON VARIABLES ----
emoji_moods = {
    "😊 Happy": "😊 Happy",
    "😢 Sad": "😢 Sad",
    "😠 Angry": "😠 Angry",
    "😌 Calm": "😌 Calm",
    "😰 Stressed": "😰 Stressed",
    "🤩 Excited": "🤩 Excited"
}

# ---- LOG MOOD PAGE ----
if page == "Log Mood":
    st.title("🌈 Mood-Based Music Journal")
    st.markdown("Track your feelings, get a motivational quote and a personalized song suggestion.")

    mood = st.radio("How are you feeling today?", list(emoji_moods.keys()), horizontal=True)

    if st.button("📥 Log Mood"):
        date = datetime.now().strftime("%Y-%m-%d")
        song, quote = get_suggestion(mood)
        save_log(date, mood, song, quote)

        st.success("✅ Mood logged successfully!")
        st.markdown(f"**🎵 Suggested Song:** {song}")
        st.markdown(f"**💬 Quote:** _{quote}_")

        # Extract artist and title for Spotify
        match = re.match(r"'(.+?)'\s*-\s*(.+)", song)
        if match:
            title_clean = match.group(1)
            artist_clean = match.group(2)
            spotify_link = get_spotify_url(title_clean, artist_clean)
            if spotify_link:
                st.markdown(f"🎧 [▶️ Listen on Spotify]({spotify_link})", unsafe_allow_html=True)
            else:
                st.warning("Couldn't find this song on Spotify.")
        else:
            st.warning("Invalid song format.")

# ---- INSIGHTS PAGE ----
elif page == "View Insights":
    st.title("📊 Mood Insights Dashboard")

    df_logs = load_logs()

    if not df_logs.empty:
        st.subheader("Mood Frequency (Last 7 Days)")
        fig = plot_mood_trend(df_logs)
        st.plotly_chart(fig, use_container_width=True)

        st.subheader("🗂️ Mood Log History")
        st.dataframe(df_logs[::-1], use_container_width=True)
    else:
        st.info("No data yet. Log your first mood to see insights.")

# ---- JOURNAL & SENTIMENT ----
elif page == "Journal & Sentiment":
    st.title("📝 Mood Journal with Sentiment Detection")

    note = st.text_area("Write freely about your feelings today:")
    if note:
        predicted_mood = get_sentiment(note)
        st.success(f"🧠 Detected Mood: **{predicted_mood}**")

        song, quote = get_suggestion(predicted_mood)
        st.markdown(f"**🎵 Suggested Song:** {song}")
        st.markdown(f"**💬 Quote:** _{quote}_")

        # Extract artist and title for Spotify
        match = re.match(r"'(.+?)'\s*-\s*(.+)", song)
        if match:
            title_clean = match.group(1)
            artist_clean = match.group(2)
            spotify_link = get_spotify_url(title_clean, artist_clean)
            if spotify_link:
                st.markdown(f"🎧 [▶️ Listen on Spotify]({spotify_link})", unsafe_allow_html=True)
            else:
                st.warning("Couldn't find this song on Spotify.")
        else:
            st.warning("Invalid song format.")

# ---- ABOUT PAGE ----
elif page == "About":
    st.title("ℹ️ About this App")
    st.markdown("""
Welcome to the **Mood-Based Music Journal** 🎧  
This app helps you:
- Log your daily mood
- Get song and quote suggestions
- Analyze mood trends over time
- Predict your mood from journal entries using sentiment analysis
- Play curated Spotify tracks based on your emotions

Built with ❤️ using:
- `Streamlit` for UI
- `Plotly` for charts
- `NLTK` for sentiment analysis
- `Spotify API` for real song recommendations

[GitHub Repo](https://github.com/Sanskrity3003/Mood_based_journal)
""")
