from tkinter import *
from tkinter import filedialog

def openFile():
    filepath = filedialog.askopenfilename(initialdir="C:\\Users\\PCC-04\\Desktop",
                                          title="You are in the desktop",
                                          filetypes=(("Text files","*.mp4"),
                                          ("All Files", "*.*"))
                                          )
    file = open(filepath, 'r')
    print(file.read())
    file.close()

window = Tk()
button = Button(text='Open', command=openFile)
button.pack()
window.mainloop()