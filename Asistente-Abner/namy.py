import speech_recognition as sr 
import pyttsx3
import pywhatkit
import pyjokes
import datetime
import subprocess as sub
import wikipedia
import os
from tkinter import *
from PIL import Image, ImageTk

main_window = Tk()
main_window.title("Abner")

main_window.geometry("1000x550")
main_window.resizable(0,0)
main_window.config(bg='#CAC531')

comandos = """
    Comandos que puedes usar:
    -Reproduce...(cancion o 
    viedeo en YT) 
    -Busca...(algo en google)
    -Entra...(pagina web o app)
    -Abrir Archivo...(Nombre)
    -Define...(algo)
    -Crea archivo...(nombre)
    -Elimina archivo...(nombre)
    -Dime un chiste
    -Finaliza
"""

label_title = Label(main_window, text="Asistente Virtual Abner", bg="#abbaab", fg="black",
                    font=('Arial', 30, 'bold'))
label_title.pack(pady=10)

canvas_comandos = Canvas(bg="#45B649", height=240, width=250)
canvas_comandos.place(x=1, y=3)
canvas_comandos.create_text(106,110, text=comandos, fill="black", font=('Arial', 12, 'bold'))

text_info = Text(main_window, bg='#86A8E7', fg="black", font=('Arial', 11, 'bold'))
text_info.place(x=0, y=250, height=300, width=252)

abner_photo = ImageTk.PhotoImage(Image.open("hola.jpg"))
window_photo = Label(main_window, image=abner_photo)
window_photo.pack(pady=5)

def mexican_voice():
    change_voice(0)
def spanish_voice():
    change_voice(2)
def english_voice():
    change_voice(1)
def change_voice(id):
    engine.setProperty('voice',voices[id].id)
    engine.setProperty('rate', 145)
    talk("hola soy abner")


name = 'Abner'
listener = sr.Recognizer()
engine = pyttsx3.init()

voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
engine.setProperty('rate', 145)

sites={
                'google':'google.com',
                'youtube':'youtube.com',
                'facebook':'facebook.com',
                'whatsapp':'web.whatsapp.com',
                'telegram':'web.telegram.com',
                'cursos':'freecodecamp.org/learn',
                'resumen': 'https://resoomer.com/es/',
                'corregir':'https://www.correctoronline.es/',
                'conclusiones': 'https://gabohedzg.github.io/'
                
            }

files={
    'mundo':'mundodesofia.pdf',
    'manual':'Manual del Estudiante Ofimatica.pdf',
    'sistema':'Sistema Nervioso.pptx',
    'analisis':'Analisis Cinetico.pptx',
    'informe':'informe final servicio social .docx',
}

programs ={
    'powerpoint': r"C:\Program Files\Microsoft Office\root\Office16\POWERPNT.EXE",
    'word': r"C:\Program Files\Microsoft Office\root\Office16\WINWORD.EXE",
    'Cisco Packet Tracer': r"C:\Program Files (x86)\Cisco Packet Tracer 6.2sv\bin\PacketTracer6.exe",
    'Excel': r"C:\Program Files\Microsoft Office\root\Office16\EXCEL.EXE"
}

def talk(text):
    engine.say(text)
    engine.runAndWait()

def habla():
    text = text_info.get("1.0","end")
    talk(text)
def escribe_text(text_wiki):
    text_info.insert(INSERT, text_wiki)


def listen(text):
    try:
        with sr.Microphone() as source:
            print(text)
            voice = listener.listen(source)
            rec = listener.recognize_google(voice, language='es-MX')
            rec = rec.lower()
               
            if name in rec:
                 rec = rec.replace(name, '')
                 print('Usted dijo: '+ rec)   
    
    except:
        pass

    return rec

def run_eva():
    while True:
        rec = listen("Esperando ordenes...")

        #videos y musica en yt
        if 'reproduce' in rec:
            music = rec.replace('reproduce', '')
            talk('Reproduciendo '+ music) 
            pywhatkit.playonyt(music)
            break

        #hora
        elif 'dime la hora actual' in rec:
            hora = datetime.datetime.now().strftime('%I:%M %p')
            talk("Son las " + hora)
            break

        #fecha
        elif 'dime la fecha actual' in rec:
            fecha = datetime.datetime.now().strftime('%d/%m/%Y')
            talk("Hoy es " + fecha)
            break

        #busqueda en google 
        elif 'busca' in rec:
            order = rec.replace('busca', '')
            talk('Buscando '+ order)
            pywhatkit.search(order)
            break
        
        #chiste
        elif 'dime un chiste' in rec:
            order = rec.replace('dime un chiste', '')
            joke = pyjokes.get_joke('es')
            talk(joke)
            escribe_text(joke)
            break


        #ejecucion de aplicaciones.exe
        if 'Ejecuta' in rec:
            order = rec.replace('ejecuta', '')
            talk('Abriendo '+ order)

            app = order+'.exe'
            os.system(app)
            break

        #creacion de directorios o carpetas 
        elif 'crea la carpeta' in rec:
            order = rec.replace
            home = "C:\\Users\\jesus\\OneDrive\\Escritorio\\carpeta\\carpeta"
            order = rec.replace('crea la carpeta', '')

            if os.path.exists(order):
                talk('la carpeta ya existe')

            else:
                mrk = os.mkdir(home+order)
                talk('La carpeta se creo correctamente')
                break

        # eliminacio de directorios o carpetas 
        elif 'elimina la carpeta' in rec:
            order = rec.replace('borra la carpeta', '')
            if os.path.exists(order):
                talk('La carpeta se elimino correctamente')
                rd = os.rmdir(order)

            else:
                talk('La carpeta no existe')
                break

        # crear achivos ".txt"
        elif 'crea el archivo' in rec:
            order = rec.replace('crea el archivo', '')
            order = order +'.txt'
            if os.path.exists(order):
                talk('El archivo ya existe')
            else:
                archivo = open(order, "w")
                archivo.close()
                talk('El archivo se creo correctamente')
                break

        #elimina archivos ".txt"
        elif 'elimina el archivo' in rec:
            order = rec.replace('elimina el archivo', '')
            order = order +'.txt'

            if os.path.exists(order):
                os.remove(order)
                talk('El archivo se elimino correctamente')

            else:
                talk('El archivo no existe')
                break

        #busqueda wiki
        elif 'explica' in rec:
            search = rec.replace('define', '')
            wikipedia.set_lang("es")
            wiki = wikipedia.summary(search, 1)
            talk(wiki)
            escribe_text(search +": " + wiki)
            break

        #Sitios web
        elif 'entra' in rec:
            for site in sites:
                if site in rec:
                    sub.call(f'start Microsoftedge.exe {sites[site]}', shell=True)
                    talk(f'Abriendo {site}')
                    break
            for app in programs:
                if app in rec:
                    talk(f'abriendo {app}')
                    os.startfile(programs[app])
                    break
        
        #Abrir archivos 
        elif 'archivo' in rec:
            for file in files:
                if file in rec:
                    sub.Popen([files[file]], shell=True)
                    talk(f'Abriendo {file}')
                    break

        elif 'termina' in rec:
            talk('adios!')
            break 

button_voice_mx = Button(main_window, text="Voz Mexico", fg="white", bg="#45a247",
                        font=("Arial", 12, "bold"), command=mexican_voice) 
button_voice_mx.place(x=750, y=80, width=100, height=30)

button_voice_es = Button(main_window, text="Voz España", fg="white", bg="#f12711",
                        font=("Arial", 12, "bold"), command=spanish_voice) 
button_voice_es.place(x=750, y=120, width=100, height=30)

button_voice_us = Button(main_window, text="Voz USA", fg="white", bg="#4286f4",
                        font=("Arial", 12, "bold"), command=english_voice) 
button_voice_us.place(x=750, y=160, width=100, height=30)

button_listen = Button(main_window, text="Escuchar", fg="white", bg="#1565C0",
                        font=("Arial", 15, "bold"), width=20, height=2, command=run_eva) 
button_listen.pack(pady=10)

button_speack = Button(main_window, text="Hablar", fg="white", bg="#1565C0",
                        font=("Arial", 12, "bold"), width=20, height=2, command=habla) 
button_speack.place(x=750, y=200, width=100, height=30)

main_window.mainloop()
