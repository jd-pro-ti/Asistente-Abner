import tkinter as tk

root = tk.Tk()
root.geometry('300x200')

text_box = tk.Text(root, height=10, width=30)
text_box.pack()

text = "Este es un ejemplo de texto que se imprimirá en el cuadro de texto."
text_box.insert(tk.END, text)

root.mainloop()