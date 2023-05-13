BACKGROUND_COLOR = "#B1DDC6"
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk
from PIL import Image
#----------------------UI Setup------------------------------#
window=Tk()
window.title("Flash Cards")
window.config(padx=50,pady=50,background=BACKGROUND_COLOR)
canvas=Canvas(width=800,height=526,highlightthickness=0,background=BACKGROUND_COLOR)
img=PhotoImage(file="./images/card_front.png")
canvas.create_image(400,263,image=img)
canvas.grid(column=1,row=0,columnspan=2)
canvas.create_text(400,140,text="French",fill="black",font=("arial",30,"bold","italic"))
canvas.create_text(400,233,text="Placeholder",fill='black',font=("arial",40,'bold'))
right=PhotoImage(file="./images/right.png")
wrong=PhotoImage(file="./images/wrong.png")
rightbutton=Button(image=right,padx=50,pady=50)
rightbutton.grid(column=2,row=2)
wrongbutton=Button(width=95,height=95,image=wrong,padx=50,pady=50,highlightthickness=0)
wrongbutton.grid(column=1,row=2)
window.mainloop()
