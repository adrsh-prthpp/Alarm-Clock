from datetime import datetime
from threading import Thread
from time import sleep
import alarm

def flash_colors():
    while True:
        window.configure(bg=color1)
        time.sleep(0.5)  # Wait for 0.5 seconds
        window.configure(bg=color2)
        time.sleep(0.5)  # Wait for 0.5 seconds

def print_alarm_message():
    print("TIME UP!")

def alarm():
    while True:
        control = 1
        print(control)

        alarm_hour = '11'
        alarm_minute = '50'
        alarm_period = 'PM'.upper()

        #setting real time
        now = datetime.now()

        hour = now.strftime("%I")
        minute = now.strftime("%M")
        period = now.strftime("%p")

        if control == 1:
            if alarm_period == period:
                if alarm_hour == hour:
                    if alarm_minute == minute:
                         print_alarm_message()
                         break
        sleep(1)

def activate_alarm():
    t = Thread(target =alarm)
    t.start()

def deactivate_alarm():
    test


#alarm()

'''

def alarm_sound():
    mixer.music.load('Alarm-Sound.mp3')
    mixer.music.play()

    mixer.init()
    alarm_sound()

    window.mainloop()

from tkinter import *
from tkinter.ttk import *
from pygame import mixer
import os

def alarm_sound():
    # Initialize mixer
    mixer.init()


    # Load and play the sound
    # Get the current directory of the script
    current_dir = os.path.dirname(os.path.abspath(__file__))

    # Construct the full path to the MP3 file
    mp3_file = os.path.join(current_dir, 'Alarm-Sound.mp3')

    # Check if the file exists
    if os.path.exists(mp3_file):
        # Load and play the sound
        mixer.music.load(mp3_file)
        mixer.music.play()

# Create the window
window = Tk()
window.title("Alarm")
window.geometry('350x150')

# Create a button to trigger the alarm sound
btn_play = Button(window, text="Play Sound", command=alarm_sound)
btn_play.pack(pady=20)

# Run the Tkinter event loop
'''
