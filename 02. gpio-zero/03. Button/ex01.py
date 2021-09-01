from gpiozero import Button
from time import sleep

button = Button(26) # 디폴트 - 내부 풀업

while True:
    if button.is_pressed:
        print("Button is pressed")
    else:
        print("Button is not pressed")
    sleep(0.5)
