from tkinter import *
from PIL import Image
from PIL import ImageTk
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps=0
timer=None
# ---------------------------- TIMER RESET ------------------------------- # 
def timer_reset():
    global reps
    window.after_cancel(timer) # type: ignore
    canvas.itemconfig(timer_text,text="00:00")
    reps=0
    label1.config(text="TIMER",fg=GREEN)
    label2.config(text="")
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def timer_start():
    global reps
    work_time=WORK_MIN*60
    short=SHORT_BREAK_MIN*60
    long=LONG_BREAK_MIN*60
    reps+=1
    if reps %2 != 0:
        count_down(work_time)
        label1.config(text="WORK!",fg=GREEN)
    elif reps % 8 == 0:
        label1.config(text="Long Break!",fg=RED)
        count_down(long)
    elif reps % 2 == 0:
        label1.config(text="Short Break!",fg=PINK)
        count_down(short)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min= int(count / 60)
    count_sec = count % 60
    if count_sec==0 or count_sec<10:
        count_sec=f"0{count_sec}"
    canvas.itemconfig(timer_text,text=f"{count_min}:{count_sec}")
    if count> 0:
        global timer
        timer=window.after(1000, count_down, count-1)
    else:
        timer_start()
        mark=''
        for _ in range (int(reps/2)):
            mark+='✔'
        label2.config(text=mark)

# ---------------------------- UI SETUP ------------------------------- #
#windows
window=Tk()
window.title("Pomodoro Timer")
window.config(padx=100,pady=50,bg=YELLOW)

#canvas
canvas=Canvas(width=200,height=224,bg=YELLOW, highlightthickness=0)
tomato_img=PhotoImage(file='tomato.png')
canvas.create_image(100,112, image=tomato_img)
timer_text=canvas.create_text(103,132,text="00:00", fill="white", font=("Courier",25,'bold','italic'))
canvas.grid(column=1, row=2)

#buttons and labels
label1=Label(text="TIMER")
label1.config(font=('Courier',28),fg=GREEN)
label1.grid(column=1,row=1)
start=Button(text="start", font=(12), command=timer_start)
start.grid(column=0,row=3)
reset=Button(text="reset", font=(12),command=timer_reset)
reset.grid(column=3,row=3)


label2=Label(fg=GREEN,bg=YELLOW)
label2.grid(column=1,row=3)

window.mainloop() 