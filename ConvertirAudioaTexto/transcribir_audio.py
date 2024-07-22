import speech_recognition as sr

# Inicializar el reconocedor
recognizer = sr.Recognizer()

# Cargar el archivo de audio convertido
audio_file_path = "PTT-20240715-WA00076.wav"  # Cambiar a "PTT-20240715-WA00076.wav"
with sr.AudioFile(audio_file_path) as source:
    audio_data = recognizer.record(source)

# Transcribir el audio
text = recognizer.recognize_google(audio_data, language="es-ES")
print(text)
