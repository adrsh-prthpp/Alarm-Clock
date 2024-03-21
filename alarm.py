from threading import Thread
from tkinter.ttk import *
from tkinter import *
import tkinter.messagebox as messagebox
import tkinter.simpledialog as simpledialog

from datetime import datetime
from time import sleep

import random

color1 = 'black'
color2 = 'white'

def get_screen_dimensions():
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    return screen_width, screen_height

window = Tk()
window.title("")
screen_width, screen_height = get_screen_dimensions()
window.geometry(f'{screen_width // 2}x{screen_height // 2}')  # Set window size to half of the screen
window.configure(bg=color2)

name = Label(window, text="ALARM", height=1, font=('Ivy 25 bold'), bg=color2)
name.place(relx=0.5, y=30, anchor='center')  # Center horizontally

hour_label = Label(window, text="HOUR", height=1, font=('Ivy 15 bold'), bg=color2, fg=color1)
hour_label.place(x=20, y=150)

c_hour = Combobox(window, width=10, font=('arial 15 bold'))
c_hour['values'] = ("00", "01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12")
c_hour.current(0)  # Set default value to "00"
c_hour.place(x=90, y=150)

minute_label = Label(window, text="MINUTE", height=1, font=('Ivy 15 bold'), bg=color2, fg=color1)
minute_label.place(x=245, y=150)

c_minute = Combobox(window, width=10, font=('arial 15 bold'))
c_minute['values'] = tuple(f"{i:02d}" for i in range(61))
c_minute.current(0)  # Set default value to "00"
c_minute.place(x=330, y=150)

period_label = Label(window, text="PERIOD", height=1, font=('Ivy 15 bold'), bg=color2, fg=color1)
period_label.place(x=490, y=150)

c_period = Combobox(window, width=10, font=('arial 15 bold'))
c_period['values'] = ("AM", "PM")
c_period.current(0)  # Set default value to "AM"
c_period.place(x=575, y=150)

def ask_math_problem():
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)
        operator = random.choice(['+', '-', '*'])
        expression = f"{num1} {operator} {num2}"

        answer = eval(expression)  # Calculate the answer

        user_response = simpledialog.askinteger("Math Problem", f"What is the answer to: {expression}?")

        if user_response is not None:  # Check if the user provided an answer
            if user_response == answer:
                messagebox.showinfo("Success", "Alarm Deactivated!")
            else:
                messagebox.showinfo("Failure", "Incorrect answer. Alarm not deactivated.")
                ask_math_problem()

def activate_alarm():
    t = Thread(target=alarm)
    t.start()



def deactivate_alarm():
    ask_math_problem()
    global running_flag  # Access the global flag
    print('Deactivated alarm: ', selected.get())
    running_flag = False  # Stop the flashing process
    window.configure(bg=color2)

selected = IntVar()

activate = Radiobutton(window, height=1, font=('arial 15 bold'), value=1, text="Activate", bg=color2,
                       command=activate_alarm, variable=selected)
activate.place(relx=0.35, y=300, anchor='center')  # Center horizontally

deactivate = Radiobutton(window, height=1, font=('arial 15 bold'), value=2, text="Deactivate", bg=color2,
                         command=deactivate_alarm, variable=selected)
deactivate.place(relx=0.65, y=300, anchor='center')  # Center horizontally


def flash_colors(window):
    def change_color():
        if running_flag:
            window.configure(bg=color1 if window.cget("bg") == color2 else color2)
            window.after(500, change_color)  # Call change_color again after 500ms

    change_color()


running_flag = True


def alarm():
    while running_flag:
        control = 1
        print(control)

        alarm_hour = c_hour.get()
        alarm_minute = c_minute.get()
        alarm_period = c_period.get()
        alarm_period = str(alarm_period).upper()

        # setting real time
        now = datetime.now()

        hour = now.strftime("%I")
        minute = now.strftime("%M")
        period = now.strftime("%p")

        if control == 1:
            if alarm_period == period:
                if alarm_hour == hour:
                    if alarm_minute == minute:
                        flash_colors(window)
                        break
        sleep(1)

window.mainloop()
