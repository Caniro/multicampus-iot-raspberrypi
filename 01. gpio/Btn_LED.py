import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

button_pin = 26
led_pin = 19

GPIO.setup(button_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(led_pin, GPIO.OUT)

light_on = False

def button_callback(channel):
    global light_on
    if light_on == False:
        GPIO.output(led_pin, 1)
        print("LED ON!")
    else:
        GPIO.output(led_pin, 0)
        print("LED OFF!")
    light_on = not light_on

GPIO.add_event_detect(button_pin, GPIO.FALLING, 
            callback=button_callback, bouncetime=300)

try:
    while 1:
        time.sleep(0.1)
finally:
    GPIO.cleanup()
