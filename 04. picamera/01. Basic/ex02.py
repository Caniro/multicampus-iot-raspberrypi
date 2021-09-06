# 파이 카메라 해상도 조절, 이미지 파일로 저장
from picamera import PiCamera
from time import sleep

with PiCamera() as camera:
    res = int(input('Resolution(1:320x240, 2:640x480, 3:1024x768)?'))
    if res == 3:
        camera.resolution = (1024, 768)
    elif res == 2:
        camera.resolution = (640, 480)
    else:
        camera.resolution = (320, 240)

    filename = input('File Name?')
    camera.start_preview()
    sleep(1)
    camera.stop_preview()
    camera.capture(filename + '.jpg')
