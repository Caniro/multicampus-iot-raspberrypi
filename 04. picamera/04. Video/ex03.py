# 영상을 mp4 포맷으로 저장
from picamera import PiCamera
from subprocess import call
import os

def convert(src, dst):
    command = f"MP4Box -add {src} {dst}"
    call([command], shell=True) # shell 명령

camera = PiCamera(resolution=(640, 480))
camera.rotation = 180

# 실행 시 워킹 디렉토리 주의
filename = 'my_video'
camera.start_recording(f"output/{filename}.h264")
camera.wait_recording(5)
camera.stop_recording()

src = f'output/{filename}.h264'
dst = f'output/{filename}.mp4'
convert(src, dst)
os.remove(src)
