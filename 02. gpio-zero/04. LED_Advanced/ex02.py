from gpiozero import LEDBoard
from signal import pause

leds = LEDBoard(12, 16, 20, 21, pwm=True)

leds.value = (0.25, 0.5, 0.75, 1.0)

pause()
