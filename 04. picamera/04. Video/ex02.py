# 영상을 mp4 포맷으로 변환
# gpac 패키지 설치해야 함 (sudo apt install -y gpac)
from subprocess import call

def convert(src, dst):
    command = f"MP4Box -add {src} {dst}"
    call([command], shell=True) # shell 명령

src = "output/my_video.h264"
dst = "output/my_video.mp4"
convert(src, dst)
