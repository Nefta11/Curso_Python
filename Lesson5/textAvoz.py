import pyttsx3

def texto_a_voz(texto):
    engine = pyttsx3.init()
    engine.say(texto)
    engine.runAndWait()

texto = input("Texto: ")
texto_a_voz(texto)