import os
import time
import tkinter as tk
import keyboard
from sound import play_sound

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> sets working directory
os.chdir(os.path.dirname(os.path.realpath(__file__)))

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> variables 
# background_color = '#cc3333'
# foreground_color = '#8b0000'
background_color = 'black'
foreground_color = 'white'
window_alpha = 15
windowtimeout = 5
font_size = 250
rel_x = 0.3


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> block input
def block_input(action):
    if action == 'block':
        keyboard.add_hotkey('alt+tab', lambda: None, suppress=True)
        keyboard.add_hotkey('alt+shift+tab', lambda: None, suppress=True)
        keyboard.add_hotkey('win+t', lambda: None, suppress=True)
        keyboard.add_hotkey('win', lambda: None, suppress=True)
        keyboard.add_hotkey('alt+f4', lambda: None, suppress=True)
        
    elif action == 'unblock':
        keyboard.clear_hotkey('alt+tab')
        keyboard.clear_hotkey('alt+shift+tab')
        keyboard.clear_hotkey('win+t')
        keyboard.clear_hotkey('win')


def start_timer():
    root = tk.Tk()
    root.attributes('-fullscreen', True)
    root.configure(bg=background_color)
    root.configure(cursor="none") 

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>  text label
    label = tk.Label(root, fg=foreground_color, bg=background_color, font=("Inter", font_size))
    label.place(relx=rel_x, rely=0.3)

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>  Function to fade in the window
    def fade_in():
        for i in range(window_alpha):
            root.attributes('-alpha', i / 10)
            root.update()
            time.sleep(0.05)
        
        play_sound('../../src/assets/audio/reward.wav')
        block_input('block')
        time.sleep(10)

    #                                                                     fade out the window
    def fade_out():
        for i in range(window_alpha, -1, -1):
            root.attributes('-alpha', i / 10)
            root.update()
            time.sleep(0.05)
        play_sound('../../src/assets/audio/level_up.wav')
        
        #                                                               >> Exit the scren
        block_input('unblock')
        root.destroy()
        time.sleep(10)

    #                                                                   start the countdown
    def countdown(time_left):
        if time_left > 0:
            play_sound('../../src/assets/audio/click.wav')

            mins, secs = divmod(time_left, 60)
            timer = '{:02d}:{:02d}'.format(mins, secs)

            label.config(text=timer)
            root.after(1000, countdown, time_left - 1)
        else:
            fade_out()

    fade_in()
    countdown(windowtimeout)  
    root.mainloop()
