# mp3 -> wav
from pydub import AudioSegment

sound = AudioSegment.from_mp3("output.mp3")
sound.export("outputFromMp3.wav", format="wav")
