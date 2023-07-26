# Import Required Library
from tkinter import *
from tkcalendar import Calendar

# Creat Ojbect
main = Tk()

# set title
main.title("GUI calendar")

# set geometry
main.geometry("400x400")

# Add Calender
cal = Calendar(main, selectmode = "day", 
               year = 2020, 
               month = 5, 
               day = 22)

cal.pack(pady = 50)

def grad_data():
    date.config(text = "Selected Data is: " + cal.get_date()) 

# Add Button and Label
Button(main, text = "Get Date",
       command = grad_data).pack(pady = 30)

date = Label(main, text = "")
date.pack(pady = 20)

# Excecute tkinter
main.mainloop()

