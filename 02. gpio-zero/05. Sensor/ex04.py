# 가까우면 led 켜기
from gpiozero import DistanceSensor, LED
from time import sleep

sensor = DistanceSensor(23, 24, max_distance=1, threshold_distance=0.2)
led = LED(13)

sensor.when_in_range = led.on
sensor.when_out_of_range = led.off

while True:
    print('Distance to nearest object is', sensor.distance, 'm')
    sleep(1)
