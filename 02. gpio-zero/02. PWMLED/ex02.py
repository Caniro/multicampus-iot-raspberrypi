from gpiozero import PWMLED
from signal import pause

led = PWMLED(13)
# led.pulse()
led.pulse(fade_in_time=3, fade_out_time=1)

pause()
