from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk

back = "white"
fore = "#65FC6A"
window = tk.Tk()
window.geometry('900x970')
top= tk.Frame(window)
top.pack(side="top")
bottom = tk.Frame(window)
bottom.pack(side="bottom")

def home(panel):
    path = 'p2.jpg'
    img = ImageTk.PhotoImage(Image.open(path))
    panel.configure(image=img)
    panel.image = img
    label.config(text= "\nPlanets\n\n")
    label.pack()

def mercury(panel):
    path = 'mercury.jpg'
    img = ImageTk.PhotoImage(Image.open(path))
    panel.configure(image=img)
    panel.image = img
    label.config(text= "\nMercury\nMercury is the smallest and fastest planet in our solar system. It is the closest planet to the Sun. It is about the size of\n"
                       "the earth's moon. \n")
    label.pack()


def venus(panel):
    path = 'venus.jpg'
    img = ImageTk.PhotoImage(Image.open(path))
    panel.configure(image=img)
    panel.image = img
    label.config(text= "\nVenus\nVenus spins slowly in the opposite direction of most planets. It is the hottest planet in our solar system because it's thick\n"
                       "atmosphere traps heat.\n")
    label.pack()


def earth(panel):
    path = 'earth.jpg'
    img = ImageTk.PhotoImage(Image.open(path))
    panel.configure(image=img)
    panel.image = img
    label.config(text= "\nEarth\nEarth is the only planet with liquid water on it's surface and it is the only planet inhabited by living things.\n")
    label.pack()


def mars(panel):
    path = 'mars.jpg'
    img = ImageTk.PhotoImage(Image.open(path))
    panel.configure(image=img)
    panel.image = img
    label.config(text= "\nMars\nMars is a cold desert-like planet. Mars used to have a thicker atmosphere that provided a wetter and warmer climate.\n")
    label.pack()


def jupiter(panel):
    path = 'jupiter.jpg'
    img = ImageTk.PhotoImage(Image.open(path))
    panel.configure(image=img)
    panel.image = img
    label.config(text= "\nJupiter\nJupiter is twice as massive as the other planets in the solar system combined. It's Great Red spot is a centuries old\n"
                       "storm bigger than earth.\n")
    label.pack()


def saturn(panel):
    path = 'saturn.jpg'
    img = ImageTk.PhotoImage(Image.open(path))
    panel.configure(image=img)
    panel.image = img
    label.config(text= "\nSaturn\nSaturn is known for it's complex system of icy rings that surround it.\n")
    label.pack()

def uranus(panel):
    path = 'uranus.jpg'
    img = ImageTk.PhotoImage(Image.open(path))
    panel.configure(image=img)
    panel.image = img
    label.config(text= "\nUranus\nUranus is the 7th planet from the Sun. It rotates at almost a 90 degree angle that makes it appear to spin on its side.\n")
    label.pack()


def neptune(panel):
    path = 'neptune.jpg'
    img = ImageTk.PhotoImage(Image.open(path))
    panel.configure(image=img)
    panel.image = img
    label.config(text= "\nNeptune\n Neptune is the 8th and farthest planet from the Sun. It is dark, cold and whipped by supersonic winds. It was the first\n"
                       "planet located through mathematical calculations.\n")
    label.pack()


path = 'planets.jpg'
img= ImageTk.PhotoImage(Image.open(path))
panel = tk.Label(window, bg= "black", fg= "black", image = img)
panel.image = img
panel.pack(side = "top", fill = "both", expand = "yes")
label = Label(window, fg= "black", text="", anchor= "n")

button1 = tk.Button(window, bg = "black", fg= back, text = "Home",command = lambda: home(panel))
button1.pack(in_= bottom, side="left")
button2 = tk.Button(window, bg = "black", fg= back, text = "Mercury",command = lambda: mercury(panel))
button2.pack(in_= bottom, side="left")
button3 = tk.Button(window, bg = "black", fg= back, text = "Venus",command = lambda: venus(panel))
button3.pack(in_= bottom, side="left")
button4 = tk.Button(window, bg = "black", fg= back, text = "Earth",command = lambda: earth(panel))
button4.pack(in_= bottom, side="left")
button5 = tk.Button(window, bg = "black", fg= back, text = "Mars",command = lambda: mars(panel))
button5.pack(in_= bottom, side="left")
button6 = tk.Button(window, bg = "black", fg= back, text = "Jupiter",command = lambda: jupiter(panel))
button6.pack(in_= bottom, side="left")
button7 = tk.Button(window, bg = "black", fg= back, text = "Saturn",command = lambda: saturn(panel))
button7.pack(in_= bottom, side="left")
button8 = tk.Button(window, bg = "black", fg= back, text = "Uranus",command = lambda: uranus(panel))
button8.pack(in_= bottom, side="left")
button9 = tk.Button(window, bg = "black", fg= back, text = "Neptune",command = lambda: neptune(panel))
button9.pack(in_= bottom, side="left")

window.mainloop()