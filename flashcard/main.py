BACKGROUND_COLOR = "#B1DDC6"
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk
from PIL import Image
import pandas as pd
import random as rand
dic={}
#----------------------data-setup----------------------------#
try:
    data_frame=pd.read_csv("/data/Words_to_learn.csv")
except:
    original_data=pd.read_csv("./data/french_words.csv")
    dic=original_data.to_dict(orient="records")
else:
    dic=data_frame.to_dict(orient="records")
current_card=rand.choice(dic)
def button_pressed():
    global current_card
    window.after_cancel(change) # type: ignore
    current_card=rand.choice(dic)
    canvas.itemconfig(canvas_image,image=img)
    canvas.itemconfig(lang,text="French",fill="black")
    canvas.itemconfig(clue,text=current_card["French"],fill="black")
    window.after(3000,change)
#----------------------flipcard----------------------------------#
#----------------------Save Progress----------------------------#
def correct():
    dic.remove(current_card)
    data=pd.DataFrame(dic)
    data.to_csv("data/Words_to_learn.csv",index=False)
    button_pressed()
def incorrect():
    button_pressed()
#-------------------------------------------------------------------#
def change():
    canvas.itemconfig(canvas_image, image=img2)
    canvas.itemconfig(lang,text="English",fill="white")
    canvas.itemconfig(clue,text=current_card["English"],fill="white")
#----------------------UI Setup------------------------------#
window=Tk()
window.title("Flash Cards")
window.config(padx=50,pady=50,background=BACKGROUND_COLOR)
canvas=Canvas(width=800,height=526,highlightthickness=0,background=BACKGROUND_COLOR)
img=PhotoImage(file="./images/card_front.png")
canvas_image=canvas.create_image(400,263,image=img)
img2=PhotoImage(file="./images/card_back.png")
canvas.grid(column=1,row=0,columnspan=2)
lang=canvas.create_text(400,120,text="French",fill="black",font=("arial",30,"bold","italic"))
clue=canvas.create_text(400,213,text=current_card["French"],fill='black',font=("arial",40,'bold'))
right=PhotoImage(file="./images/right.png")
wrong=PhotoImage(file="./images/wrong.png")
rightbutton=Button(image=right,padx=50,pady=50,highlightbackground=BACKGROUND_COLOR,highlightthickness=0,command=correct)
rightbutton.grid(column=2,row=2)
wrongbutton=Button(width=95,height=95,image=wrong,padx=50,pady=50,highlightthickness=0,command=incorrect)
wrongbutton.grid(column=1,row=2)
window.after(3000,change)
window.mainloop()

#--------------------------------------------------------#
