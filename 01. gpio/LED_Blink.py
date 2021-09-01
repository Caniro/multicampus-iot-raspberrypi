import RPi.GPIO as GPIO
import time

led_green = 19
led_red = 13

GPIO.setmode(GPIO.BCM)

GPIO.setup(led_green, GPIO.OUT)
GPIO.setup(led_red, GPIO.OUT)

try:
    for i in range(10):
        GPIO.output(led_green, 1)
        GPIO.output(led_red, 0)
        time.sleep(1)
        GPIO.output(led_green, 0)
        GPIO.output(led_red, 1)
        time.sleep(1)
finally:
    GPIO.cleanup()
