# 비디오 캡처
import cv2
from datetime import datetime

cap = cv2.VideoCapture(0) # 0번 카메라
# cap = cv2.VideoCapture('./data/vtest.avi') # 영상 파일
# cap = cv2.VideoCapture('http://192.168.117.22:4747/video') # droid cam
# cap.set(cv2.CAP_PROP_FRAME_WIDTH, 320)
# cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 240)

frame_size = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)),
            int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))

print('frame_size = ', frame_size)

while True:
    retval, frame = cap.read() # 프레임 캡처
    if not retval: break
    current_time = datetime.now().strftime("%Y%m%d_%H%M%S.avi")
    cv2.putText(frame, current_time, (20, 30), 
                0, 0.5, (0, 255, 0))
    cv2.imshow('frame', frame)
    key = cv2.waitKey(25)
    if key == 27: break # ESC키를 누른 경우 루프 탈출

if cap.isOpened():
    cap.release()

cv2.destroyAllWindows()
