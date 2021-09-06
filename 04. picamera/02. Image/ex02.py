# 스트림으로 캡처
# 파일처럼 다루지만 (파일 포인터 존재: tell, seek 등)
# 메모리 상에 존재한다.
from io import BytesIO
from picamera import PiCamera

my_stream = BytesIO()

camera = PiCamera()
camera.capture(my_stream, 'jpeg')

print(my_stream.tell())
# 파일로 저장하려면 위치를 처음으로 옮겨야 한다. (rewind)
my_stream.seek(0)
print(my_stream.tell())

with open('output/capture.jpg', 'wb') as f:
    f.write(my_stream.read())
