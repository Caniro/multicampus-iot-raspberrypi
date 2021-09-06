# 영상을 .h264 포맷으로 저장
from picamera import PiCamera

camera = PiCamera(resolution=(640, 480))
camera.rotation = 180

# 실행 시 워킹 디렉토리 주의
camera.start_recording('output/my_video.h264')
camera.wait_recording(5)
camera.stop_recording()
