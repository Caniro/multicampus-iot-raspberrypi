# PIL(Python Image Library) 객체 활용
from io import BytesIO
from picamera import PiCamera
from PIL import Image

stream = BytesIO()

camera = PiCamera()
print(camera.resolution)    # 기본 해상도 확인
camera.rotation = 180       # 180도 회전

camera.capture(stream, format='jpeg')

stream.seek(0)              # rewind
image = Image.open(stream)
image.show()                # 임시파일 형태로 열린다.
