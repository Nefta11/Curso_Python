from pydub import AudioSegment
import speech_recognition as sr

# Load the .opus file
audio = AudioSegment.from_file("PTT-20240715-WA0007.opus")

# Export the audio as .wav
audio.export("audio.wav", format="wav")

# Initialize recognizer
recognizer = sr.Recognizer()

# Load the audio file
audio_file_path = "audio.wav"
with sr.AudioFile(audio_file_path) as source:
    audio_data = recognizer.record(source)

# Transcribe the audio
text = recognizer.recognize_google(audio_data, language="es-ES")
print(text)
