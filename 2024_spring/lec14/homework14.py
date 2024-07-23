import datetime
from gtts import gTTS
import librosa
import IPython.display as ipd

def what_time_is_it(lang: str, filename: str) -> None:
    """
    Generate an audio file that says the current time in the specified language.

    Parameters:
    lang (str): Language code (e.g., 'en' for English, 'ja' for Japanese).
    filename (str): Filename to save the audio file.
    """
    current_time = datetime.datetime.now().strftime("%H:%M")
    text = f"The current time is {current_time}" if lang == 'en' else f"現在の時刻は {current_time} です"
    
    tts = gTTS(text, lang=lang)
    tts.save(filename)

def tell_me_a_joke(lang: str, audiofile: str) -> None:
    """
    Generate an audio file that tells a joke in the specified language.

    Parameters:
    lang (str): Language code (e.g., 'en' for English).
    audiofile (str): Filename to save the audio file.
    """
    joke = "Why don't scientists trust atoms? Because they make up everything." if lang == 'en' else "科学者は原子を信じていないのはなぜですか？なぜなら、彼らはすべてを構成しているからです。"
    
    tts = gTTS(joke, lang=lang)
    tts.save(audiofile)

def what_day_is_it(lang: str, audiofile: str) -> None:
    """
    Generate an audio file that says the current day in the specified language.

    Parameters:
    lang (str): Language code (e.g., 'en' for English, 'ja' for Japanese).
    audiofile (str): Filename to save the audio file.
    """
    current_day = datetime.datetime.now().strftime("%A")
    text = f"Today is {current_day}" if lang == 'en' else f"今日は {current_day} です"
    
    tts = gTTS(text, lang=lang)
    tts.save(audiofile)

def personal_assistant(lang: str, filename: str) -> None:
    """
    Run the personal assistant which tells the time, a joke, and the day.

    Parameters:
    lang (str): Language code (e.g., 'en' for English, 'ja' for Japanese).
    filename (str): Base filename to save the audio files (e.g., 'output' will save 'output_time.mp3', 'output_joke.mp3', 'output_day.mp3').
    """
    what_time_is_it(lang, f"{filename}_time.mp3")
    tell_me_a_joke(lang, f"{filename}_joke.mp3")
    what_day_is_it(lang, f"{filename}_day.mp3")
    
    # Load the audio files and play them (assuming they were saved correctly)
    x, fs = librosa.load(f"{filename}_time.mp3")
    ipd.Audio(data=x, rate=fs)
    x, fs = librosa.load(f"{filename}_joke.mp3")
    ipd.Audio(data=x, rate=fs)
    x, fs = librosa.load(f"{filename}_day.mp3")
    ipd.Audio(data=x, rate=fs)

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 3:
        print("Usage: python homework14.py <lang> <filename>")
    else:
        lang = sys.argv[1]
        filename = sys.argv[2]
        personal_assistant(lang, filename)
