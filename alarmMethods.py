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

name = Label(window, text = "Alarm", height=1, font=('Ivy 18 bold'), bg=color2)
name.place(x=125,y=10)

hour = Label(window, text = "hour", height=1, font=('Ivy 10 bold'), bg=color2, fg=color1)
hour.place(x=127,y=40)
c_hour = Combobox(window, width=2, font=('arial 15'))
c_hour['values'] = ("00", "01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11","12" )
c_hour.current(0)
c_hour.place(x=130, y=58)

minute = Label(window, text = "minute", height=1, font=('Ivy 10 bold'), bg=color2, fg=color1)
minute.place(x=177,y=40)
c_minute = Combobox(window, width=2, font=('arial 15'))
c_minute['values'] = (['00', '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', 
                       '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', 
                       '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44', '45', '46', '47', 
                       '48', '49', '50', '51', '52', '53', '54', '55', '56', '57', '58', '59', '60'])
c_minute.current(0)
c_minute.place(x=180, y=58)

period = Label(window, text = "period", height=1, font=('Ivy 10 bold'), bg=color2, fg=color1)
period.place(x=230,y=40)
c_period = Combobox(window, width=3, font=('arial 15'))
c_period['values'] = ("AM", "PM")
c_period.current(0)
c_period.place(x=230, y=58)

def activate_alarm():
    t = Thread(target =alarm)
    t.start()

def deactivate_alarm(window):
     print('Deactivated alarm: ', selected.get())
     window.configure(bg=color1)

selected = IntVar()

activate = Radiobutton(window, height=1, font=('arial 10 bold'), value = 1, text = "Activate", bg=color2, command=activate_alarm, variable=selected)
activate.place(x=125,y=95)

deactivate = Radiobutton(window, height=1, font=('arial 10 bold'), value = 2, text = "Deactivate", bg=color2, command=deactivate_alarm, variable=selected)
deactivate.place(x=187,y=95)

def flash_colors(window):
    def change_color():
        window.configure(bg=color1 if window.cget("bg") == color2 else color2)
        window.after(500, change_color)  # Call change_color again after 500ms
    change_color()

def print_alarm_message():
    print("TIME UP!")

def alarm():
    while True:
        control = 1
        print(control)

        alarm_hour = c_hour.get()
        alarm_minute = c_minute.get()
        alarm_period = c_period.get()
        alarm_period = str(alarm_period).upper()

        #setting real time
        now = datetime.now()

        hour = now.strftime("%I")
        minute = now.strftime("%M")
        period = now.strftime("%p")

        if control == 1:
            if alarm_period == period:
                if alarm_hour == hour:
                    if alarm_minute == minute:
                         flash_colors(window)
                         print_alarm_message()
                         break
        sleep(1)

window.mainloop()

#alarm()
