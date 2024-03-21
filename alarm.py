from threading import Thread
from tkinter.ttk import *
from tkinter import *

from datetime import datetime
from time import sleep

color1 = 'black'
color2 = 'white'

window = Tk()
window.title("")
window.geometry('350x150')
window.configure(bg=color2)

name = Label(window, text="Alarm", height=1, font=('Ivy 18 bold'), bg=color2)
name.place(relx=0.5, y=10, anchor='center')  # Center horizontally

hour_label = Label(window, text="hour", height=1, font=('Ivy 10 bold'), bg=color2, fg=color1)
hour_label.place(x=20, y=40)

c_hour = Combobox(window, width=2, font=('arial 15'))
c_hour['values'] = ("00", "01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12")
c_hour.current(0)  # Set default value to "00"
c_hour.place(x=55, y=40)

minute_label = Label(window, text="minute", height=1, font=('Ivy 10 bold'), bg=color2, fg=color1)
minute_label.place(x=110, y=40)

c_minute = Combobox(window, width=2, font=('arial 15'))
c_minute['values'] = tuple(f"{i:02d}" for i in range(61))
c_minute.current(0)  # Set default value to "00"
c_minute.place(x=160, y=40)

period_label = Label(window, text="period", height=1, font=('Ivy 10 bold'), bg=color2, fg=color1)
period_label.place(x=215, y=40)

c_period = Combobox(window, width=3, font=('arial 15'))
c_period['values'] = ("AM", "PM")
c_period.current(0)  # Set default value to "AM"
c_period.place(x=265, y=40)


def activate_alarm():
    t = Thread(target=alarm)
    t.start()


def deactivate_alarm():
    global running_flag  # Access the global flag
    print('Deactivated alarm: ', selected.get())
    running_flag = False  # Stop the flashing process
    window.configure(bg=color2)

selected = IntVar()

activate = Radiobutton(window, height=1, font=('arial 10 bold'), value=1, text="Activate", bg=color2,
                       command=activate_alarm, variable=selected)
activate.place(relx=0.35, y=95, anchor='center')  # Center horizontally

deactivate = Radiobutton(window, height=1, font=('arial 10 bold'), value=2, text="Deactivate", bg=color2,
                         command=deactivate_alarm, variable=selected)
deactivate.place(relx=0.65, y=95, anchor='center')  # Center horizontally


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
