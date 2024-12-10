from tkinter import *
from tkinter import filedialog
from tkinter import ttk

def create_window():
    Toplevel()


def openFile():
    filepath = filedialog.askopenfilename(initialdir="C:\\Users\\PCC-04",
                                          title="You are in the desktop",
                                          filetypes=(("Text files","*.mp4"),
                                          ("All Files", "*.*"))
                                          )
    
    file = open(filepath, 'r')
    print(file.read())
    file.close()
    
def saveFile():
    file = filedialog.asksaveasfile(initialdir="C:\\Users\\PCC-04",
                                    defaultextension=".txt",
                                    filetypes=[
                                        ("Text file", ".txt"),
                                        ("HTML file", ".html"),
                                        ("All Files", ".*")
                                        ])

def cut():
    print("You cut some text")   
def copy():
    print("You copied some text")   
def paste():
    print("You pasted some text")   
    
window = Tk()
window.title("Feazy's App")

# openImage = PhotoImage(file="file.png")
# saveImage = PhotoImage(file="save.png")
# exitImage = PhotoImage(file="exit.png")

menubar = Menu(window)
window.config(menu=menubar)

fileMenu= Menu(menubar,tearoff=0,font=("MV Boli",12))
menubar.add_cascade(label="File", menu=fileMenu)
fileMenu.add_command(label="New Window",
                     command=create_window)
fileMenu.add_command(label="open",
                     command=openFile, 
                    #  image=openImage,
                     compound='left'
                     )
fileMenu.add_command(label="save",
                     command=saveFile, 
                    #  image=saveImage,
                     compound='left'
                     )
fileMenu.add_separator()
fileMenu.add_command(label="exit",
                     command=quit, 
                    #  image=exitImage,
                     compound='left'
                     )

editMenu = Menu(menubar, tearoff=0,font=("MV Boli",12))
menubar.add_cascade(label="Edit", menu=editMenu)
editMenu.add_command(label="Cut",command=cut)
editMenu.add_command(label="Copy",command=copy)
editMenu.add_command(label="Paste",command=paste)

notebook = ttk.Notebook(window)  #

tab1 = Frame(notebook) 
tab2 = Frame(notebook) 

notebook.add(tab1, text="tab1")
notebook.add(tab2, text="tab2")
notebook.pack(expand=True) 

Label(tab1,text="Hello this tab # 1", width=50, height=25).pack()
Label(tab2,text="Goodbye this tab # 2", width=50, height=25).pack()



window.mainloop()

