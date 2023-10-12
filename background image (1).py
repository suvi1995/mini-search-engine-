#Using Canvas

from tkinter import *
from PIL import ImageTk, Image
w = Tk()
w.geometry("1980x1080")

c = Canvas(w, width=1980, height=1080, bg='white')
c.grid(row=2, column=3)

img = ImageTk.PhotoImage(Image.open("image.jpg"))  # PIL solution
c.create_image(0, 0, anchor=NW, image=img)



