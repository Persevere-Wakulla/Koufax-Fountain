from tkinter import *


def display():
    if x.get() == 1:
        print("You agree!")
    else:
        print("You dont agree :(")


window = Tk()

x = IntVar()

# python_photo = PhotoImage(file='python.png')

check_button = Checkbutton(
    window,
    text="I agree to something",
    variable=x,
    onvalue=1,
    offvalue=0,
    command=display,
    font=("Arial", 20),
    fg="#00ff00",
    bg="black",
    activeforeground="#00ff00",
    activebackground="black",
    padx=25,
    pady=10,
    #    image=python_photo,
    compound="left",
)
check_button.pack()

window.mainloop()
