# 캡처 시 이미지 크기 조정
from picamera import PiCamera

camera = PiCamera()
camera.resolution = (1024, 768)

camera.capture('output/foo.jpg', resize=(320, 240))
