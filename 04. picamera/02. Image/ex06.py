# 연속 이미지 캡처 - capture_sequence
from picamera import PiCamera

camera = PiCamera(resolution=(1280, 720), framerate=30)

camera.iso = 100

camera.shutter_speed = camera.exposure_speed
camera.exposure_mode = 'off'
g = camera.awb_gains
camera.awb_mode = 'off'
camera.awb_gains = g

camera.capture_sequence([f'output/image{i:02d}.jpg' for i in range(10)])
