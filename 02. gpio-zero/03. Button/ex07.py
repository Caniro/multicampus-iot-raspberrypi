# 버튼 토글
from gpiozero import LED, Button
from signal import pause

led = LED(13)
button = Button(26)

button.when_pressed = led.toggle # 인스턴스의 메서드를 콜백으로 등록 - C++에서는 안된다.

pause()
