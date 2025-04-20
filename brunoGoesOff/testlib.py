import librosa
import vlc
import time
import math

y, sr = librosa.load('C:\\Users\\megha\\wonderwaller\\LOOH.mp3')

tempo, beatFrames = librosa.beat.beat_track(y=y, sr=sr)
beatFrames = [math.floor(fr) for fr in beatFrames] 

beatTimes = librosa.frames_to_time(beatFrames, sr=sr)

bruno = vlc.MediaPlayer("LOOH.mp3")
bruno.play()

beat_num = 0

start = time.time() - 0.18

for i in beatTimes:
    print(i)

while beat_num < len(beatTimes):
    current_time = time.time() - start
    beat_time = beatTimes[beat_num]

    if abs(current_time - beat_time) <= 0.2:
        snare = vlc.MediaPlayer("snare.mp3")
        snare.play()
        print(f"beat {beat_num=}")
        beat_num += 1  

    time.sleep(1/100)