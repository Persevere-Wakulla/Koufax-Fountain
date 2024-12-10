from tkinter import *

#label = an area widget that holds text and/or an image within the window

window = Tk()

# photo = PhotoImage(file='C:\\Users\\PCC-04\\Desktop\\K2-18b.png')

label = Label(window,
              text="Hello",
              font=('Arial',40,'bold'),
              fg='#00FF00',
              bg='black',
              relief=RAISED,
              bd=10,
              padx=20,
              pady=20,
            #   image=photo,
              compound='bottom')
label.pack()
# label.place(x=100,y=100)


window.mainloop()
