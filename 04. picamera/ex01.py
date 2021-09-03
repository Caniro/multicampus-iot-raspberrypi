# 파이 카메라 인식 테스트 및 미리보기
from picamera import PiCamera
from time import sleep

camera = PiCamera()
#camera.rotation = 180 # 180도 회전
print(camera.resolution)
camera.start_preview()
# camera.start_preview(alpha=200) # 투명도 : 0 ~ 255
sleep(1)
camera.stop_preview()
