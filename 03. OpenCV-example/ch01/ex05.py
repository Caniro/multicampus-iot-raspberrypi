# 버튼을 누르면 녹화 시작
# 버튼을 떼면 녹화 종료
# 수정 필요 (영상 안나옴)
import cv2
from datetime import datetime
from gpiozero import Button
from signal import pause
from time import sleep

cap = cv2.VideoCapture(0) # 0번 카메라
frame_size = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)),
            int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
print('frame_size = ', frame_size)
fourcc = cv2.VideoWriter_fourcc(*'XVID')

button = Button(26) # 디폴트 - 내부 풀업
start = 0
out = ""
is_recording = False

def start_record():
    global start, out, is_recording
    start = datetime.now()
    fname = start.strftime("%Y%m%d_%H%M%S.avi")
    print('녹화 시작', fname)
    out = cv2.VideoWriter(f'./data/{fname}', fourcc, 20.0, frame_size)

    is_recording = True
    while is_recording:
        retval, frame = cap.read() # 프레임 캡처
        if not retval: break
        out.write(frame)
        cv2.imshow('CCTV', frame)
        cv2.waitKey(25)

def stop_record():
    global is_recording
    is_recording = False
    sleep(0.5)
    end = datetime.now()
    print("녹화 중지(녹화 시간)", end - start)
    cap.release()
    out.release()
    cv2.destroyAllWindows()

button.when_pressed = start_record
button.when_released = stop_record

pause()
