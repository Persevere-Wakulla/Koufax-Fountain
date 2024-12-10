# radio button = similar to checkbox, but you can only select one from a group
from tkinter import *

food = ["pizza", "hamburger", "hotdog"]

def order():
    if(x.get() == 0):
        print("You ordered pizza")
    elif(x.get() == 1):
        print("You ordered a hamburger")
    elif(x.get() == 2):
        print("You ordered a hotdog")
    else:
        print("huh?")

# pizzaImage = PhotoImage(file='pizza.png')
# hamburgerImage = PhotoImage(file='hamburger.png')
# hotdogImage = PhotoImage(file='hotdog.png')
# foodImages = [pizzaImage, hamburgerImage, hotdogImage]

window = Tk()

x = IntVar()

for index in range(len(food)):
    radiobutton = Radiobutton(window,
                               text=food[index], #adds text to radio buttons
                               variable=x, #groups radio buttons together if they share the same variable
                               value=index, #assigns each radio button a different value
                               padx= 25,
                               font=("impact",50),
                            #    image= foodImages[index] #adds image to radiobutton,
                               compound="left", #add image to left side
                               indicatoron=0, #eliminate circle indicator
                               width=375, #sets width of radio buttons
                               command=order #set command of radio button to function
                               ) 
    radiobutton.pack(anchor=W)

window.mainloop()