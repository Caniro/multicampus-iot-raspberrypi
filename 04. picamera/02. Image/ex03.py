# 파일로 캡처 (미리 open해놓고 객체를 인자로 넘김)
from picamera import PiCamera

with open('output/my_image.jpg', 'wb') as my_file:
    camera = PiCamera()
    camera.capture(my_file)
