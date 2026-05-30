import io
import speech_recognition as sr
import pyttsx3


def synthesize_speech(text: str, voice_rate: int = 160) -> bytes:
    engine = pyttsx3.init()
    engine.setProperty("rate", voice_rate)
    buffer = io.BytesIO()
    engine.save_to_file(text, "output_audio.wav")
    engine.runAndWait()
    with open("output_audio.wav", "rb") as f:
        audio = f.read()
    return audio


def transcribe_audio(file_bytes: bytes) -> str:
    recognizer = sr.Recognizer()
    with sr.AudioFile(io.BytesIO(file_bytes)) as source:
        audio = recognizer.record(source)
    return recognizer.recognize_google(audio)
