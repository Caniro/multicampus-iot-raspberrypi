# wav 파일 재생
from pydub import AudioSegment
from pydub.playback import play

song = AudioSegment.from_file("output.wav", format="wav")
# song = AudioSegment.from_wav("output.wav")

play(song)
