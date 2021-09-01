from gpiozero import LEDBoard
from time import sleep
from signal import pause

leds = LEDBoard(12, 16, 20, 21)

leds.on()
sleep(1)
leds.off()
sleep(1)

leds.value = (1, 0, 1, 0)
sleep(1)
leds.blink()

pause()
