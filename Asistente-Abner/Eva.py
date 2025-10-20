import speech_recognition as sr 
import pyttsx3
import pywhatkit
import pyjokes
import datetime
import subprocess as sub
import wikipedia
import os


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
                'cursos':'freecodecamp.org/learn'
            }

files={
    'mundo':'mundodesofia.pdf',
    'manual':'Manual del Estudiante Ofimatica.pdf',
    'sistema':'Sistema Nervioso.pptx',
    'analisis':'Analisis Cinetico.pptx',
    'informe':'informe final servicio social .docx'
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
            print(joke)
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
        elif 'define' in rec:
            search = rec.replace('define', '')
            wikipedia.set_lang("es")
            wiki = wikipedia.summary(search, 1)
            print(search +": " + wiki)
            talk(wiki)
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

#iniciador 
if __name__ == '__main__':
    run_eva()
