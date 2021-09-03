# 비디오 녹화
from picamera import PiCamera

with PiCamera() as camera:
    res = int(input('Resolution(1:320x240, 2:640x480, 3:1024x768)?'))
    if res == 3:
        camera.resolution = (1024, 768)
    elif res == 2:
        camera.resolution = (640, 480)
    else:
        camera.resolution = (320, 240)
    filename = input('File Name?')

    camera.framerate = 30 # 낮으면 왜 빨리감기한 것처럼..?
    camera.hflip = True
    camera.vflip = True
    camera.start_recording(output = filename + '.h264')
    camera.wait_recording(10)
    camera.stop_recording()

# vflip이나 hflip은 의도치않게 좌우 혹은 상하가 바뀌기 때문에,
# 주로 거울모드로 쓸 때 사용한다.
# 그 외에는 camera.rotation = 180 등으로 각도를 조절하여 사용한다.
