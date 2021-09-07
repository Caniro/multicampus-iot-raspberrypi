from pyaudio import PyAudio, paInt16
import wave

CHUNK = 1024                # 버퍼
FORMAT = paInt16            # 음질 bit depth
CHANNELS = 1                # 모노 채널
# RATE = 44100                # 샘플 레이트
RATE = 16000                # 카카오 API에서는 16000Hz로 고정, 음성 식별 가능 수준

RECORD_SECONDS = 5
WAVE_OUTPUT_FILENAME = "output.wav"

p = PyAudio()
stream = p.open(
                # input_device_index=2, # 16000Hz로 녹음 시에는 기본 녹음 장치를 선택하고 이걸 주석처리해야 함
                frames_per_buffer=CHUNK,
                format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True)

# 음량 조절 명령어 : alsamixer
print("Recording...")
frames = []
for i in range(0, int(RATE * RECORD_SECONDS / CHUNK)):
    data = stream.read(CHUNK, exception_on_overflow=False)
    frames.append(data)
stream.stop_stream()
stream.close()
p.terminate()
print("Finished recording!")

# wav 파일로 저장
with wave.open(WAVE_OUTPUT_FILENAME, 'wb') as wf:
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
print(f"Finished saving {WAVE_OUTPUT_FILENAME}")
