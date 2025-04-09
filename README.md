# 🎵 Mood-Based Music Journal

A **simple yet powerful Streamlit app** that helps you log your mood daily and receive a personalized **music + motivational quote** suggestion. It also tracks your emotional trends visually using Plotly — turning self-care into a habit. 💚



---

## 🌟 Features

- 🧠 **Mood Logging**: Select your mood with emojis (e.g. 😊, 😢, 😡, 😌).
- 🎶 **Music + Quote Suggestions**: Get curated songs and motivational quotes for your current mood.
- 📊 **Mood Trend Visualization**: See weekly trends with a beautiful interactive bar graph (Plotly).
- 📁 **Mood History**: Your entries are logged in a CSV file for personal tracking.
- 🚀 **Hosted with Streamlit Cloud**: Works entirely in-browser. No installations needed!

---

## 🛠 Tech Stack

| Tool/Library     | Purpose                      |
|------------------|------------------------------|
| **Python**        | Core programming language     |
| **Streamlit**     | Interactive web app framework |
| **Plotly**        | Data visualization (bar charts) |
| **Pandas**        | Data processing & reading CSV |
| **CSV**           | Simple mood logging storage    |
| **GitHub**        | Version control & deployment   |

---


## 📂 Project Structure

```
mood_journal/
├── app.py                # Main Streamlit app
├── suggestions.py        # Mood-based suggestions (songs + quotes)
├── mood_utils.py         # Utility functions (logging, data handling)
├── mood_log.csv          # Data log of moods (auto-created)
├── requirements.txt      # Python dependencies
└── README.md             # You're here!
```

---

## 🚀 How to Run Locally

### 1. Clone the Repo

```bash
git clone https://github.com/sanskrity3003/mood-journal.git
cd mood-journal
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the App

```bash
streamlit run app.py
```

The app will open in your browser at `http://localhost:8501`

---

## 🌐 Live App

Access the live app here:  
**🔗 [mood-journal.streamlit.app](https://moodbasedjournal-jrnra6vqwupn4tgenlseq7.streamlit.app/)**

---

## ✨ Future Ideas

- 🎧 Integrate with Spotify API to play actual songs.
- 📬 Daily email reminders to log your mood.
- 🧠 Sentiment analysis from user-written journal entries.
- ☁️ Move from CSV to Firebase/Google Sheets for cloud logging.

---

## 🙌 Author

Built with ❤️ by **[Sanskriti Yadav](https://github.com/sanskrity3003)**

If you liked this project, give it a ⭐ and share your feedback!

---
