from tkinter import *

window=Tk()
window.title("Miles to Kilometre")
window.minsize(height=200,width=400)
window.config(padx=100,pady=100)
input = Entry(width=10)
input.grid(column=2,row=2)

label=Label(text="Miles")
label.grid(column=3,row=2)
label1=Label(text="is equal to")
label1.grid(column=1,row=3)

def button_used():
    e=input.get()
    con=round(int(e)*1.609)
    label3=Label(text=con)
    label3.grid(column=2,row=3)
button=Button(text="calculate",command=button_used)
button.grid(column=2,row=5)

label4=Label(text="Kilometers")
label4.grid(column=3,row=3)
window.mainloop()