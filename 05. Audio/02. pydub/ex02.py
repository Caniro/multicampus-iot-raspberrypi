# mp3 파일 재생
from pydub import AudioSegment
from pydub.playback import play

# song = AudioSegment.from_file("output.mp3", format="mp3")
song = AudioSegment.from_mp3("output.mp3")

play(song)
