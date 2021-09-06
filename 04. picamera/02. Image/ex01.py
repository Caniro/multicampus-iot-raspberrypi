# jpg 파일로 캡처 (파일명을 인자로 넘김)
from picamera import PiCamera

camera = PiCamera()
camera.resolution = (1024, 768)

camera.capture('output/foo.jpg')
