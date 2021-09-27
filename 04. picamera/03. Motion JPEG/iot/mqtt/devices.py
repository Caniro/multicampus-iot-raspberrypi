from . import add_topic_handler
from gpiozero import AngularServo
from gpiozero.pins.pigpio import PiGPIOFactory
from .car import Car

# PiGPIOFactory : 지터링 방지. 전담 프로세스로 
factory = PiGPIOFactory(host='localhost')

servo = AngularServo(16, pin_factory=factory,
                    min_angle=90, max_angle=-90,
                    min_pulse_width=0.00045, max_pulse_width=0.0023)

def move_angle(topic, value):
    angle = int(value)
    servo.angle = angle

car = Car()

def move_car(topic, value):
    print(topic, value)
    car.move(value)
