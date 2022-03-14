#Importing all the necessary libraries 
from tkinter import *
import datetime
import time
import winsound

def alarm(set_alarm_timer):
    while True:
        time.sleep(1)
        current_time = datetime.datetime.now()
        now = current_time.strftime("%H:%M:%S")
        date = current_time.strftime("%d/%m/%Y")
        print("The Set Date is:",date)
        print(now)
        if now == set_alarm_timer:
            print("Time to Wake up")
            winsound.PlaySound("sound.wav",winsound.SND_ASYNC)
            break

def actual_time():
    set_alarm_timer = f"{hour.get()}:{min.get()}:{sec.get()}"
    alarm(set_alarm_timer)

clock = Tk()
clock.title("1810991680_Akul Goyal")
clock.geometry("400x200")
cname=Label(clock, text= "Alarm Clock", fg="red",bg="black",font="Arial").place(x=130,y=0)
time_format=Label(clock, text= "Enter time in 24 hour format!", fg="red",bg="black",font="Arial").place(x=60,y=30)
addTime = Label(clock,text = "Hour  Min   Sec",font=60).place(x = 110, y=65)
setYourAlarm = Label(clock,text = "When to wake you up",fg="blue",font=("Helevetica",7,"bold")).place(x=0, y=89)

# The Variables we require to set the alarm
hour = StringVar()
min = StringVar()
sec = StringVar()

#Time required to set the alarm
hourTime= Entry(clock,textvariable = hour,bg = "pink",width = 15).place(x=110,y=90)
minTime= Entry(clock,textvariable = min,bg = "pink",width = 15).place(x=150,y=90)
secTime = Entry(clock,textvariable = sec,bg = "pink",width = 15).place(x=200,y=90)

#To take the time input by user
submit = Button(clock,text = "Set Alarm",fg="white",bg="black",width = 10,command = actual_time).place(x =110,y=120)

clock.mainloop()
#Execution of the window