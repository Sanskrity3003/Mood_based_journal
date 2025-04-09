import random

mood_suggestions = {
    "😊 Happy": [
        ("'Happy' - Pharrell Williams", "Smile big, you deserve it!"),
        ("'Good Vibrations' - Beach Boys", "Keep shining, you’re doing great!"),
    ],
    "😢 Sad": [
        ("'Fix You' - Coldplay", "Tough times don’t last. You do."),
        ("'Someone Like You' - Adele", "Let it out and let it go."),
    ],
    "😠 Angry": [
        ("'Smells Like Teen Spirit' - Nirvana", "Breathe. You are in control."),
        ("'Breaking the Habit' - Linkin Park", "Let the music help you cool down."),
    ],
    "😌 Calm": [
        ("'Weightless' - Marconi Union", "Peace begins with a deep breath."),
        ("'River Flows In You' - Yiruma", "Stillness speaks volumes."),
    ],
    "😰 Stressed": [
        ("'Let It Be' - The Beatles", "You are doing your best."),
        ("'Breathe Me' - Sia", "Pause. Reset. Restart."),
    ],
    "🤩 Excited": [
        ("'Uptown Funk' - Bruno Mars", "Ride that high!"),
        ("'On Top of the World' - Imagine Dragons", "Energy like yours is contagious!"),
    ],
}

def get_suggestion(mood):
    return random.choice(mood_suggestions.get(mood, [("🎵 Music is healing", "You got this! ❤️")]))
