from tkinter import *

window = Tk() #instantiate an instance of a window
window.geometry("420x420")
window.title("Koufax's first GUI program")

# icon = PhotoImage(file='pic.jpg') #to replace icon in windobar
# window.iconphoto(True,icon)
window.config(background="#5cfcff")

window.mainloop() #this will place window on computer screen and listen to events