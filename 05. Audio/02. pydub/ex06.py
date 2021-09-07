# 서버에서 mp3 데이터 수신 시뮬레이션

from pydub import AudioSegment
from pydub.playback import play
from io import BytesIO

def receive():
    f = open('output.mp3', 'rb')
    return f.read()

audio = BytesIO(receive())
song = AudioSegment.from_mp3(audio)
play(song)
