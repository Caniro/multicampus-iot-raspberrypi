import RPi.GPIO as GPIO
import time

button_pin = 26
led_green = 19

GPIO.setmode(GPIO.BCM)

GPIO.setup(button_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(led_green, GPIO.OUT)

try:
    while 1:
        if GPIO.input(button_pin) == GPIO.LOW:
            GPIO.output(led_green, 1)
            print("Button pushed!")
            time.sleep(0.1)
        GPIO.output(led_green, 0)
finally:
    GPIO.cleanup()
