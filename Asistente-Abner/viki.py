import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import os
import pyjokes 

name = "viki"
listener = sr.Recognizer()
engine = pyttsx3.init()

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    try:
        with sr.Microphone() as source:
            print("Esperando ordenes...")
            pc = listener.listen(source)
            rec = listener.recognize_google(pc, language="es-MX")
            rec = rec.lower()
            
            if name in rec:
                rec = rec.replace(name, '')
                print('usted dijo: '+ rec)


    except:
        pass
    return rec

def run_viki():
    while True:
        rec = listen()
        if 'reproduce' in rec:
                music = rec.replace('reproduce', '')
                print('Reproduciendo '+ music)
                talk('Reproduciendo '+ music) 
                pywhatkit.playonyt(music)
        
        
    


if __name__ == '__main__':
    run_viki()
