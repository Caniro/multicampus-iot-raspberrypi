import sounddevice as sd

# print(sd.default.device)
# print(sd.default.samplerate)
# print(sd.default.channels)

duration = 5.5 # seconds

# indata : 녹음된 데이터 (numpy 배열)
# outdata : 출력용 데이터 (callback 함수 끝나고 outdata가 존재하면 Stream에서 재생)
def callback(indata, outdata, frames, time, status):
    if status:
        print(status)
        outdata[:] = indata

with sd.Stream(channels=1, callback=callback):
    sd.sleep(int(duration * 1000))
