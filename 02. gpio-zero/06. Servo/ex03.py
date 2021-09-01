from gpiozero import AngularServo
from time import sleep

servo = AngularServo(21,
            min_angle=-90, max_angle=90,
            min_pulse_width=0.00054, max_pulse_width=0.0024) # 조이스틱 연결 시 -90도 ~ 90도가 유용

while True:
    servo.angle = -90
    sleep(2)
    servo.angle = 0
    sleep(2)
    servo.angle = 90
    sleep(2)
    servo.angle = 0
    sleep(2)
