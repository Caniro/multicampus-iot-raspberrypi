# 텍스트 쓰기
from picamera import PiCamera, Color
from time import sleep

camera = PiCamera()

camera.start_preview()

camera.annotate_text_size = 50
camera.annotate_background = Color('blue')
camera.annotate_foreground = Color('white')
camera.annotate_text = "Hello world"
sleep(1)
camera.capture('text.jpg')

camera.stop_preview()
