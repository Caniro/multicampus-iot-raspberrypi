# PIR 센서로 움직임이 감지되면 녹화, 파일 저장 시뮬레이션
from gpiozero import MotionSensor, LED
from signal import pause
from datetime import datetime

pir = MotionSensor(12)
led = LED(19)
start = 0

def start_record():
    led.on()
    global start
    start = datetime.now()
    fname = start.strftime("%Y%m%d_%H%M%S.avi")
    print('녹화 시작', fname)
    # 카메라 녹화 시작
    pass

def stop_record():
    led.off()
    end = datetime.now()
    print("녹화 중지(녹화 시간)", end - start)
    # 녹화 중지
    pass

pir.when_motion = start_record
pir.when_no_motion = stop_record

pause()
