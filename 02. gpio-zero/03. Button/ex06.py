from gpiozero import LED, Button
from signal import pause

led = LED(13)
button = Button(26)

led.source = button

pause()
