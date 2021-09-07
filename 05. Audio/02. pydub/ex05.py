# wav -> mp3 (BytesIO 사용)
from pydub import AudioSegment
from pydub.playback import play
from io import BytesIO
import requests

# 지금은 파일로 읽지만 네트워크에서 수신된 데이터 처리도 가능
with open("output.wav", "rb") as f:
    wavMem = BytesIO(f.read())

mp3Mem = BytesIO()
sound = AudioSegment.from_file(wavMem, format="wav")
sound.export(mp3Mem, format="mp3", codec="libmp3lame")

mp3Mem.read(5000)       # 5KB 지점부터 시작
print(mp3Mem.tell())
# mp3Mem.seek(0)          # 처음부터 시작

song = AudioSegment.from_mp3(mp3Mem)
play(song)
