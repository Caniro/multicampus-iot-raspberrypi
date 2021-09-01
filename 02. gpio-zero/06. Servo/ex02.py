from gpiozero import Servo
from time import sleep
# servo = Servo(21, min_pulse_width=0.00054, max_pulse_width=0.0024) # 0 ~ 180
servo = Servo(21, min_pulse_width=0.00054, max_pulse_width=0.0023) # 경계값에서는 동작이 불안정하므로 오차 여유
while True:
    servo.value = 0
    print("mid")
    sleep(0.5)
    servo.value = -1
    print("min")
    sleep(1)
    servo.value = 0
    print("mid")
    sleep(0.5)
    servo.value = 1
    print("max")
    sleep(1)
