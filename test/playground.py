from tkinter import *

window = Tk()
window.title("Test")
window.minsize(height=300, width=500)

# def button_clicked():
# return ("I got clicked")


label = Label(text="Text")
label.pack()

input = Entry(width=10)
input.pack()

def button_clicked():
    label.config(text=input.get())


button = Button(text="click me", command=button_clicked)
button.pack()

entry=Entry(width=30)
entry.insert(END,string="Some text to begin with")
print(entry.get())

text=Text(width=30,height=5)
text.insert(END,"Example of multiline text")
print(text.get("1.0",END))

def spinbox_used():
    print(spinbox.get())
spinbox=Spinbox(from_=0,to=100,width=5,command=spinbox_used)
spinbox.pack()

def scale_used():
    print(scale.get())
scale=Scale(from_=0,to=100,command=scale_used)
scale.pack()

def check_button_used():
    print(checked_state.get())
checked_state=IntVar()
check_button=Checkbutton(text="is it on?",variable=checked_state,command=check_button_used)
checked_state.get()
check_button.pack()

def radio_button_used():
    print(radio_state.get())
radio_state=IntVar()
radio_button1=Radiobutton(text="Option 1",value=1,variable=radio_state,command=radio_button_used)
radio_button2=Radiobutton(text="option 2", value=2, variable=radio_state,command=radio_button_used)
radio_button1.pack()
radio_button2.pack(side='left')
window.mainloop()