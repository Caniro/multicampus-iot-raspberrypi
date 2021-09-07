# 음량 시각화
import sounddevice as sd
import numpy as np

duration = 30

def print_sound(indata, outdata, frames, time, status):
    volume_norm = np.linalg.norm(indata) * 10
    print("|" * int(volume_norm))

with sd.Stream(callback=print_sound):
    sd.sleep(duration * 1000)
