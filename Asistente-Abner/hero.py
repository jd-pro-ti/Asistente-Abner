import speech_recognition as sr
import pyttsx3

# Initialize the speech recognition and text-to-speech engines
r = sr.Recognizer()
tts = pyttsx3.init()

# Define a function to get voice input and convert it to text
def get_input():
    with sr.Microphone() as source:
        print("¿En qué puedo ayudarte?")
        audio = r.listen(source)
        text = r.recognize_google(audio, language='es-ES')
        return text.lower()

# Define a function to respond with text-to-speech
def respond(message):
    print("Asistente: " + message)
    tts.say(message)
    tts.runAndWait()

# Define your assistant's behavior
while True:
    try:
        # Get voice input
        input_text = get_input()
        
        # Define your assistant's responses
        if "hola" in input_text:
            respond("¡Hola! ¿En qué puedo ayudarte?")
        elif "adiós" in input_text:
            respond("¡Hasta luego!")
            break
        else:
            respond("Lo siento, no entiendo lo que quieres decir.")
    except sr.UnknownValueError:
        respond("Lo siento, no he podido entenderte. ¿Podrías repetirlo, por favor?")