import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

led_pin = 13
GPIO.setup(led_pin, GPIO.OUT)

freq = 50
p = GPIO.PWM(led_pin, freq)
p.start(0)

try:
    while 1:
        for dc in range(0, 101, 5):
            p.ChangeDutyCycle(dc)
            time.sleep(0.1)
        for dc in range(100, -1, -5):
            p.ChangeDutyCycle(dc)
            time.sleep(0.1)
except KeyboardInterrupt:
    pass

p.stop()
GPIO.cleanup()
