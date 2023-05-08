
from tkinter import *
from tkinter import messagebox
from PIL import Image
from PIL import ImageTk
from pyperclip import copy

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    pass_text.delete(0,END)
    import random
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    #for char in range(nr_letters):
    #  password_list.append(random.choice(letters))
    #####random.shuffle(password_list)
    pasword_letters=[random.choice(letters) for x in range(nr_letters)]
    pasword_symbols=[random.choice(symbols) for x in range(nr_symbols)]
    pasword_numbers=[random.choice(numbers) for x in range(nr_numbers)]

    password_list=pasword_letters+pasword_numbers+pasword_symbols
    random.shuffle(password_list)
    password = "".join(password_list)
    copy(password)
    pass_text.insert(0,string=password)



# ---------------------------- SAVE PASSWORD ------------------------------- #
def details():
    a=web_text.get()
    b=em_text.get()
    c=pass_text.get()
    if len(a) == 0 or len(c) ==0:
        pop=messagebox.showerror(title="Oops", message="Don't leave any fields empty")
        return
    is_ok=messagebox.askokcancel(title=a, message=f"These are the details entered: \n{b}\n{c}\n Do you want to save?")
    if is_ok:
        with open("password.txt",'a') as f:
            f.write(f"{a}||{b}||{c}\n")
            web_text.delete(0,END)
            pass_text.delete(0,END)
# ---------------------------- UI SETUP ------------------------------- #

window=Tk()
window.title("Password Manager")
window.config(padx=45,pady=45)
canvas=Canvas(width=400,height=400)
img=PhotoImage(file='logo.png')
canvas.create_image(200,200,image=img)
canvas.grid(column=1,row=0)
web=Label(text="Website:")
web.grid(column=0,row=1,sticky="e")
web_text=Entry(width=45)
web_text.focus()
web_text.grid(row=1,column=1,columnspan=2,sticky="w")
em=Label(text="Email:")
em.grid(column=0,row=2,sticky="e")
em_text=Entry(width=45)
em_text.grid(row=2,column=1,columnspan=2,sticky="w")
em_text.insert(0,string="remudeysdemha97@gmail.com")
passw=Label(text="Password:")
passw.grid(column=0,row=3,sticky="e")
pass_text=Entry(width=21)
pass_text.grid(row=3,column=1,sticky="w",columnspan=2)
gen=Button(text="Generate Password",width=18, command=generate_password)
gen.grid(column=1,row=3,columnspan=2)
add=Button(text="Add",width=30, command=details)
add.grid(column=1,row=4,sticky="w",columnspan=2)

window.mainloop()