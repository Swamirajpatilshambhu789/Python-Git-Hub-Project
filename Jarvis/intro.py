from tkinter import * #pip install tkinter
from PIL import Image,ImageTk,ImageSequence #pip install Pillow
import time
import pygame  #pip install pygame
from pygame import mixer
mixer.init()

root = Tk()
root.geometry("1000x600")

def play_gif():
    root.lift()
    root.attributes("-topmost",True)
    global img
    img = Image.open("intro.jpg")
    lbl = Label(root)
    lbl.place(x=0,y=0)
    i=0
    mixer.music.load("Iron man landing sound effects.mp3")
    mixer.music.play()
    
    for img in ImageSequence.Iterator(img):
        img = img.resize((1000,600))
        img = ImageTk.PhotoImage(img)
        lbl.config(image=img)
        root.update()
        time.sleep(5)
    root.destroy()

play_gif()
root.mainloop()