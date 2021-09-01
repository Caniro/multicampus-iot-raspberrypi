import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

buzzer_pin = 6
GPIO.setup(buzzer_pin, GPIO.OUT)

freq = 100
p = GPIO.PWM(buzzer_pin, freq)

octab = [ 262, 294, 330, 349, 392, 440, 493, 523 ]
speed = 0.5

p.start(10)

try:
    while 1:
        for m in octab:
            p.ChangeFrequency(m)
            time.sleep(speed)
            p.ChangeFrequency(10)
            time.sleep(0.05)
except KeyboardInterrupt:
    pass

p.stop()
GPIO.cleanup()
