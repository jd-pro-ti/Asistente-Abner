import speech_recognitionas as sr
import pyttsx3, pywhatkit

name = "abner"
listener =sr.Recognizer()
engine =pyttsx3.init()

voices = engine.getProperty(voices)
 ngine.setProperty('voice', voices[0].id)

def talk(text):
    engine.say(text)
    engine.runandwait()

def listen():
    try:
        with sr.Microphone() source
            print("Escuchando...")
            pc = listener(source)
            rec = listener.recognize_google(pc)
            rec =rec. lower()
            if name in rec:
                rec =rec.replace(name, '')e
     
    except:
        pass 
    return rec 

def run_aber():
    rec = listen()
    if 'reproduce' in rec:
    music =rec.replace('reproduce', '')
    print("reproduciendo "+ music)
    talk(*Reproduciendo  + music) 
    pywhatkit.playyonyt(music) 

 if _0
_name__ == '__main__':
    run_abner()