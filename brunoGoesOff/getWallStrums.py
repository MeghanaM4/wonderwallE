import librosa
import vlc
import time
import math
import keyboard

log_file = 'keystrokes.txt'

with open('keystrokes.txt', 'w') as file:
    file.write('')

start = time.time()
wallE = vlc.MediaPlayer("wonderwall.mp3")
wallE.play()

def on_space_press(event):
    print(time.time() - start)
    with open(log_file, 'a') as f:
        f.write('{}\n'.format(time.time() - start))

keyboard.on_press_key("space", on_space_press)

keyboard.wait()

