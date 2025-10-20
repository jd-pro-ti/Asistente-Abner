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

main_window.geometry("900x550")
main_window.resizable(0,0)
main_window.config(bg='#8E2DE2')

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

label_title = Label(main_window, text="Abner", bg="#6DD5FA", fg="#41295a",
                    font=('Arial', 30, 'bold'))
label_title.pack(pady=10)

canvas_comandos = Canvas(bg="#4e54c8", height=200, width=200)
canvas_comandos.place(x=0, y=1)
canvas_comandos.create_text(90,94, text=comandos, fill="black", font='Arial 11')

text_info = Text(main_window, bg='#4e54c8', fg="black", font=('Arial', 11, 'bold'))
text_info.place(x=0, y=200, height=350, width=202)

abner_photo = ImageTk.PhotoImage(Image.open("Abner2.jpg"))
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

sites = dict()

files = dict()

programs = dict()

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
            talk("TE ESCUCHO")
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
        elif 'Define' in rec:
            search = rec.replace('define', '')
            wikipedia.set_lang("es")
            wiki = wikipedia.summary(search, 1)
            talk(wiki)
            escribe_text(search +": " + wiki)
            break

        #Sitios web
        elif 'entra' in rec:
            task = rec.replace('entra', '').strip()
            
            if task in sites:
                for task in sites:
                    if task in rec:
                        sub.call(f'start Microsoftedge.exe {sites[task]}', shell=True)
                        talk(f'Abriendo {task}')
                        break
            elif task in programs:
                for task in programs:
                    if task in rec:
                        talk(f'abriendo {task}')
                        os.startfile(programs[task])
            else:
                talk("lo siento, no has agregado esa pagina o app, usa los botones de agregar")
                break
        
        #Abrir archivos 
        elif 'archivo' in rec:
            file = rec.replace('archivo', '').strip()
            if file in files:
                for file in files:
                    if file in rec:
                        sub.Popen([files[file]], shell=True)
                        talk(f'Abriendo {file}')
            else:
                talk("lo siento, no has agregado ese archivo, usa el boton de agregar archivo")
                break

        elif 'Finaliza' in rec:
            talk('ADIOS!!!')
            break 

def open_w_files():
    global namefile_entry, pathf_entry
    windows_files = Toplevel()
    windows_files.title("Agregar Archivos")
    windows_files.configure(bg="#434343")
    windows_files.geometry("300x200")
    windows_files.resizable(0,0)
    main_window.eval(f'tk::PlaceWindow {str(windows_files)} center')

    title_label = Label(windows_files, text="Agregar un archivo", bg="#6DD5FA", fg="#434343", font=('Arial', 15, 'bold'))
    title_label.pack(pady=3)
    name_label  = Label(windows_files, text="Agregar un archivo", bg="#6DD5FA", fg="#434343", font=('Arial', 11, 'bold'))
    name_label.pack(padx=2)

    namefile_entry = Entry(windows_files)
    namefile_entry.pack(padx=1)

    path_label  = Label(windows_files, text="Ruta del archivo", bg="#6DD5FA", fg="#434343", font=('Arial', 11, 'bold'))
    path_label.pack(padx=2)

    pathf_entry = Entry(windows_files, width=35)
    pathf_entry.pack(padx=1)

    save_button = Button(windows_files, text="Guardar", fg="white", bg="#16222A",
                        font=("Arial", 9, "bold"), width=8, height=1, command=add_files)
    save_button.pack(padx=4)

def open_w_apps():
    global nameapp_entry, patha_entry
    windows_apps = Toplevel()
    windows_apps.title("Agregar Apps")
    windows_apps.configure(bg="#434343")
    windows_apps.geometry("300x200")
    windows_apps.resizable(0,0)
    main_window.eval(f'tk::PlaceWindow {str(windows_apps)} center')

    title_label = Label(windows_apps, text="Agregar una app", bg="#6DD5FA", fg="#434343", font=('Arial', 15, 'bold'))
    title_label.pack(pady=3)
    name_label  = Label(windows_apps, text="Nombtre de la app", bg="#6DD5FA", fg="#434343", font=('Arial', 11, 'bold'))
    name_label.pack(padx=2)

    nameapp_entry = Entry(windows_apps)
    nameapp_entry.pack(padx=1)

    path_label  = Label(windows_apps, text="Ruta de la app", bg="#6DD5FA", fg="#434343", font=('Arial', 11, 'bold'))
    path_label.pack(padx=2)

    patha_entry = Entry(windows_apps, width=35)
    patha_entry.pack(padx=1)

    save_button = Button(windows_apps, text="Guardar", fg="white", bg="#16222A",
                        font=("Arial", 9, "bold"), width=8, height=1, command=add_apps)
    save_button.pack(padx=4)


def open_w_pages():
    global namepages_entry, paths_entry
    windows_pages = Toplevel()
    windows_pages.title("Agregar Pagina web")
    windows_pages.configure(bg="#434343")
    windows_pages.geometry("300x200")
    windows_pages.resizable(0,0)
    main_window.eval(f'tk::PlaceWindow {str(windows_pages)} center')

    title_label = Label(windows_pages, text="Agregar una pagina web", bg="#6DD5FA", fg="#434343", font=('Arial', 15, 'bold'))
    title_label.pack(pady=3)
    name_label  = Label(windows_pages, text="Nombre de la pagina web", bg="#6DD5FA", fg="#434343", font=('Arial', 11, 'bold'))
    name_label.pack(padx=2)

    namepages_entry = Entry(windows_pages)
    namepages_entry.pack(padx=1)

    path_label  = Label(windows_pages, text="URL de la pagina", bg="#6DD5FA", fg="#434343", font=('Arial', 11, 'bold'))
    path_label.pack(padx=2)

    paths_entry = Entry(windows_pages, width=35)
    paths_entry.pack(padx=1)

    save_button = Button(windows_pages, text="Guardar", fg="white", bg="#16222A",
                        font=("Arial", 9, "bold"), width=8, height=1, command=add_pages)
    save_button.pack(padx=4)

def add_files():
    name_file = namefile_entry.get().strip()
    path_file = pathf_entry.get().strip()
    
    files[name_file] = path_file
    namefile_entry.delete(0, "end")
    pathf_entry.delete(0, "end")

def add_apps():
    name_file = nameapp_entry.get().strip()
    path_file = patha_entry.get().strip()
    
    programs[name_file] = path_file
    nameapp_entry.delete(0, "end")
    patha_entry.delete(0, "end")


def add_pages():
    name_pages = namepages_entry.get().strip()
    Url_pages = paths_entry.get().strip()
    
    sites[name_pages] = Url_pages
    namepages_entry.delete(0, "end")
    paths_entry.delete(0, "end")


#butones de imagen
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

#fff
button_add_files = Button(main_window, text="Agregar archivos", fg="white", bg="#1565C0",
                        font=("Arial", 12, "bold"), width=20, height=2, command=open_w_files) 
button_add_files.place(x=732, y=240, width=140, height=30)

button_add_apps = Button(main_window, text="Agregar apps", fg="white", bg="#1565C0",
                        font=("Arial", 12, "bold"), width=20, height=2, command=open_w_apps) 
button_add_apps.place(x=732, y=280, width=140, height=30)

button_add_pages = Button(main_window, text="Agregar paginas", fg="white", bg="#1565C0",
                        font=("Arial", 12, "bold"), width=20, height=2, command=open_w_pages) 
button_add_pages.place(x=732, y=320, width=140, height=30)


main_window.mainloop()