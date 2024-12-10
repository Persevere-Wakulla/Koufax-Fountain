from tkinter import *

def submit():
    print("The temp is: " + str(scale.get()) + " degrees c")

window = Tk()

# hotImage = PhotoImage(file='hot.png') 
# hotLabel = Label(image=hotImage)
# hotLabel.pack()


scale = Scale(window,
              from_=100, 
              to=0,
              length=600,
              orient=VERTICAL,#Orientation of scale
              font=("Consoles",20),
              tickinterval=10, #adds numeric indicators for value
              showvalue=0, #hide current value
              resolution=5, #increment of slider
              troughcolor="#69eaff",
              fg="#ff1c00",
              bg='black'
              ) 
      
scale.set(((scale['from']-scale['to'])/2) + scale['to'])      
        
scale.pack()

# coldImage = PhotoImage(file='cold.png') 
# coldLabel = Label(image=coldImage)
# coldLabel.pack()

button = Button(window, text="Submit", command=submit)
button.pack()

window.mainloop()