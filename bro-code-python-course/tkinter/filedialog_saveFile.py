from tkinter import *
from tkinter import filedialog

def saveFile():
    file = filedialog.asksaveasfile(initialdir="C:\\Users\\PCC-04\\Desktop\\Koufax Fountain",
                                    defaultextension=".txt",
                                    filetypes=[
                                        ("Text file", ".txt"),
                                        ("HTML file", ".html"),
                                        ("All Files", ".*")
                                    ])
    if file is None:
        return
    filetext = str(text.get(1.0,END))
    # filetext = input("Enter some text: ")
    file.write(filetext)
    file.close()

window = Tk()
button = Button(text='save',command=saveFile)
button.pack()
text = Text()
text.pack()
window.mainloop()