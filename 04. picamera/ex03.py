# 이미지로 저장, with 사용
from picamera import PiCamera
from time import sleep

with PiCamera() as camera:
    camera.start_preview()
    for i in range(5):
        sleep(3)
        camera.capture(f'image_{i}.jpg')
    camera.stop_preview()
