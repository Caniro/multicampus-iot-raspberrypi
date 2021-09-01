from gpiozero import LED
from signal import pause

red = LED(13)
# red.blink()
red.blink(on_time=0.1, off_time=0.1)

try:
    pause()
except KeyboardInterrupt:
    pass

print("\b\bThis message is not printed")
