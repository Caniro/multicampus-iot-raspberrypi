# 연속 이미지 캡처 - capture_continuous
from picamera import PiCamera
from time import sleep

camera = PiCamera()

for filename in camera.capture_continuous('output/img{counter:03d}.jpg'):
    print(f'Captured {filename}')
    sleep(3)
