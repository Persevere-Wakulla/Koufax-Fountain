from tkinter import *

def create_window():
    new_window = Tk()     #Toplevel() #new window on top of other window, 
#                       linked to a bottom window
    old_window.destroy() #will close out of old window

old_window = Tk()

Button(old_window,text="Create new window",command=create_window).pack()

old_window.mainloop()