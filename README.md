
---

# 🎵 **Mood-Based Music Journal**

A simple yet powerful **Streamlit** app that helps you log your mood daily and receive a personalized music + motivational quote suggestion. It also tracks your emotional trends visually using **Plotly** — turning self-care into a habit. 💚

## 🌟 **Features**

- 🧠 **Mood Logging**: Select your mood with emojis (e.g. 😊, 😢, 😡, 😌).
- 🎶 **Music + Quote Suggestions**: Get curated songs and motivational quotes for your current mood.
- 📊 **Mood Trend Visualization**: See weekly trends with a beautiful interactive bar graph (Plotly).
- 📁 **Mood History**: Your entries are logged in a CSV file for personal tracking.
- 🎧 **Spotify Integration**: Listen to your personalized song suggestions directly on Spotify.
- 🧠 **Sentiment Analysis**: Write a journal entry, and the app will detect your mood using sentiment analysis.
- 🚀 **Hosted with Streamlit Cloud**: Works entirely in-browser. No installations needed!

## 🛠 **Tech Stack**

| Tool/Library | Purpose                                      |
|--------------|----------------------------------------------|
| Python       | Core programming language                    |
| Streamlit    | Interactive web app framework                |
| Plotly       | Data visualization (bar charts)              |
| Pandas       | Data processing & reading CSV                |
| CSV          | Simple mood logging storage                  |
| Spotipy      | Spotify API integration for song search      |
| VADER        | Sentiment analysis for journal entries       |
| GitHub       | Version control & deployment                 |

## 📂 **Project Structure**

```
mood_journal/
├── app.py                # Main Streamlit app
├── suggestions.py        # Mood-based suggestions (songs + quotes)
├── mood_utils.py         # Utility functions (logging, data handling)
├── mood_log.csv          # Data log of moods (auto-created)
├── requirements.txt      # Python dependencies
└── README.md             # You're here!
```

## 🚀 **How to Run Locally**

1. **Clone the Repo**  
   Clone the repository to your local machine:

   ```bash
   git clone https://github.com/sanskrity3003/mood-journal.git
   cd mood-journal
   ```

2. **Install Dependencies**  
   Install the required Python libraries:

   ```bash
   pip install -r requirements.txt
   ```

3. **Run the App**  
   Start the Streamlit app:

   ```bash
   streamlit run app.py
   ```

   The app will open in your browser at [http://localhost:8501](http://localhost:8501).

## 🌐 **Live App**

Access the live app here:  
🔗 [mood-journal.streamlit.app]([https://mood-journal.streamlit.app](https://moodbasedjournal-jrnra6vqwupn4tgenlseq7.streamlit.app/))

## ✨ **Future Ideas**

- 📬 **Daily email reminders** to log your mood and stay motivated.
- ☁️ Move from **CSV to Firebase/Google Sheets** for cloud logging.
- 📱 Mobile app integration for better accessibility.

## 🙌 **Author**

Built with ❤️ by **Sanskriti Yadav**

If you liked this project, give it a ⭐ and share your feedback!

----
