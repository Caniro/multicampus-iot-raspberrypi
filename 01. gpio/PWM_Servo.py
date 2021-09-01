import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

servo_pin = 14
GPIO.setup(servo_pin, GPIO.OUT)

servo = GPIO.PWM(servo_pin, 50)
servo.start(0)

def move_angle(angle):
    servo.ChangeDutyCycle(angle / 18 + 2.5)

try:
    while 1:
        # servo.ChangeDutyCycle(7.5)
        # time.sleep(1)
        # servo.ChangeDutyCycle(12.5)
        # time.sleep(1)
        # servo.ChangeDutyCycle(2.5)
        # time.sleep(1)
        move_angle(90)
        time.sleep(1)
        move_angle(180)
        time.sleep(1)
        move_angle(0)
        time.sleep(1)
except KeyboardInterrupt:
    pass

servo.stop()
GPIO.cleanup()
