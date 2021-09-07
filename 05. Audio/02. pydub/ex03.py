# wav -> mp3
from pydub import AudioSegment

sound = AudioSegment.from_wav("output.wav")
sound.export("output.mp3", format="mp3", codec="libmp3lame")
