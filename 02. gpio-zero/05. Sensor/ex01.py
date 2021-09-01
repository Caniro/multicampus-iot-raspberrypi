from gpiozero import MotionSensor, LED
from signal import pause

pir = MotionSensor(12)
led = LED(19)

pir.when_motion = led.on
pir.when_no_motion = led.off

pause()
