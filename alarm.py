from tkinter.ttk import *
from tkinter import *

from pygame import mixer

from PIL import ImageTk, Image

import alarmMethods

#colors
color1 = 'black'
color2 = 'white'

#window
window = Tk()
window.title("")
window.geometry('350x150')
window.configure(bg=color2)

'''
#frame up
frame_line = Frame(window, width=400, height=5, bg=color1)
frame_line.grid(row=0, column=0)

frame_body = Frame(window, width=400, height=290, bg=color2)
frame_body.grid(row=1, column=0)

#configure frame body

img = Image.open('alarm-clock.png')
img.resize((100,100))
img = ImageTk.PhotoImage(img)


app_image = Label(frame_body, height= 100, image=img, bg=bg_color)
app_image.place(x=10, y=10)
'''
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

selected = IntVar()
activate = Radiobutton(window, height=1, font=('arial 10 bold'), value = 1, text = "Activate", bg=color2, command=alarmMethods.activate_alarm)
activate.place(x=125,y=95)


window.mainloop()
