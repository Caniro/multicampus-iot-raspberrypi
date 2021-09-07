# 볼륨에 따라 기록 여부 결정
# 왜 Ctrl + C 안되지
import io
import queue
import sounddevice as sd
import soundfile as sf
import sys
import numpy as np

samplerate = 16000
channels = 1
sd.default.samplerate = samplerate
sd.default.device = 1
# sd.default.device = '마이크(USB PnP Sound Device), MME'
sd.default.channels = channels
q = queue.Queue()
recMem = io.BytesIO()
def callback(indata, frames, time, status):
    if status:
        print(status, file=sys.stderr)
    volume_norm = np.linalg.norm(indata) * 10
    if (volume_norm > 3):
        print("음성 감지")
        q.put(indata.copy()) # 녹음 데이터 큐에 추가

try:
    with sf.SoundFile(recMem, mode='x', format='wav',
            samplerate=samplerate, channels=channels) as file:
        with sd.InputStream(callback=callback):
            print('#' * 80)
            print('press Ctrl+C to stop the recording')
            print('#' * 80)
            while True:
                # 큐에 녹음 데이터가 있다면 추출하여 파일에 기록
                file.write(q.get())
except KeyboardInterrupt:
    print(recMem.tell())
    # 완료 처리
    print('\nRecording finished: ')
except Exception as e:
    print(e)
