##################### Extra Hard Starting Project ######################
import pandas as pd
import smtplib
import random as rand
from tkinter import *
# 1. Update the birthdays.csv
data=pd.read_csv("birthdays.csv")
details=data.to_dict(orient="records")

window=Tk()
window.title("Email adder")
label1=Label(text="Email Adder!")
label1.grid(column=1,row=0)
l2=Label(text="Email:")
l2.grid(column=0,row=1)

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.




