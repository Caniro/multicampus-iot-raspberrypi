import RPi.GPIO as GPIO
import time

def button_callback(channel):
    print(f"{channel} Button pushed!")

GPIO.setmode(GPIO.BCM)

button_pin = 26
GPIO.setup(button_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

GPIO.add_event_detect(button_pin, GPIO.FALLING, 
            callback=button_callback, bouncetime=300)

try:
    while 1:
        time.sleep(0.1)
finally:
    GPIO.cleanup()
