import smtplib
import random as rand
import datetime as dt
my_email="remudeys97@gmail.com"
password="tijksvrncntcxava"
now=dt.datetime.now()
day=now.weekday()
quotes_list=[]
with open("quotes.txt","r") as quotes:
    data=quotes.read()
    quotes_list=data.split("\n")
quote_of_the_day=rand.choice(quotes_list)
if day==0:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email,password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs="remudeys@yahoo.com", 
                            msg=f"Subject:Quote of the Day\n\n{quote_of_the_day}")

