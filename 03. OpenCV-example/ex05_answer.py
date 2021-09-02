# 버튼을 누르면 녹화 시작
# 버튼을 떼면 녹화 종료
from gpiozero import Button
import cv2
from datetime import datetime

recorder = None          # VideoWritter 객체
recording_status = False # 녹화 중인지 여부

cap = cv2.VideoCapture(0) # 0번 카메라
frame_size = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)),
            int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
fourcc = cv2.VideoWriter_fourcc(*'XVID')

def start_record():
    global recorder, recording_status
    start = datetime.now()
    fname = start.strftime("%Y%m%d_%H%M%S.avi")
    recorder = cv2.VideoWriter(f'./data/{fname}', fourcc, 20.0, frame_size)
    recording_status = True


def stop_record():
    global recorder, recording_status
    recording_status = False
    if recorder:
        recorder.release()
        recorder = None

button = Button(26) # 디폴트 - 내부 풀업
button.when_pressed = start_record
button.when_released = stop_record

while True:
    retval, frame = cap.read() # 프레임 캡처
    if not retval: break

    if recording_status:
        recorder.write(frame)

    cv2.imshow('frame', frame)
    key = cv2.waitKey(25)
    if key == 27: break

cap.release()

cv2.destroyAllWindows()
