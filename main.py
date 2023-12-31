
import tkinter as tk
from PIL import Image,ImageTk

import random

root=tk.Tk()
root.geometry("2000x2000")
root.title("Dice Roller Simulator")

dice=["Dice-Simulator\DiceImg\d1.png","Dice-Simulator\DiceImg\d2.png","Dice-Simulator\DiceImg\d3.png","Dice-Simulator\DiceImg\d4.png","Dice-Simulator\DiceImg\d5.png","Dice-Simulator\DiceImg\d6.png"]
image1=ImageTk.PhotoImage(Image.open(random.choice(dice)))
image2=ImageTk.PhotoImage(Image.open(random.choice(dice)))


label1=tk.Label(root,image=image1)
label2=tk.Label(root,image=image2)

label1.place(x=40,y=100)
label2.place(x=700,y=100)

def dice_roll():
    image1=ImageTk.PhotoImage(Image.open(random.choice(dice)))
    label1.configure(image=image1)
    label1.image=image1

    image2=ImageTk.PhotoImage(Image.open(random.choice(dice)))
    label2.configure(image=image2)
    label2.image=image2

button=tk.Button(root,text="Roll Dice",bg="black",fg="white",font="Verdana 20 bold",highlightcolor="black",highlightbackground="white",relief="raised",command=dice_roll)
button.place(x=545,y=30)
root.mainloop()