'''
from tkinter.ttk import *
from tkinter import *

from pygame import mixer

#window
window = Tk()
window.title("")
window.geometry('350x150')

def alarm_sound():
    mixer.music.load('Alarm-Sound.mp3')
    mixer.music.play()

    mixer.init()
    alarm_sound()

    window.mainloop()
'''
from tkinter import *
from tkinter.ttk import *
from pygame import mixer

def alarm_sound():
    # Initialize mixer
    mixer.init()


    # Load and play the sound
    mp3_file = r'C:\Users\prathap\Downloads\war-siren-mechanical-wave-1-00-49.mp3'

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
window.mainloop()
