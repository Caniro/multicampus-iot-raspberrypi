# 연속 이미지 캡처 - 타임스탬프 기능
from picamera import PiCamera
from time import sleep

camera = PiCamera()

for filename in camera.capture_continuous( \
    'output/img{timestamp:%Y-%m-%d-%H-%M-%S}.jpg'):
    print(f"Captured {filename}")
    sleep(3)
