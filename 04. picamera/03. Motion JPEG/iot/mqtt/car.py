from gpiozero import Robot

class Car:
    def __init__(self):
        self.control = Robot(left=(3, 4, 2), right=(17, 27, 22))
        self.speed = 0.7

    def move_tl(self):
        print('move top left')
        self.control.left_motor.backward(self.speed)
        self.control.right_motor.backward(self.speed * 0.8)

    def move_u(self):
        print('move forward')
        self.control.backward(self.speed)

    def move_tr(self):
        print('move top right')
        self.control.left_motor.backward(self.speed * 0.8)
        self.control.right_motor.backward(self.speed)

    def move_l(self):
        print('move left')
        self.control.left(self.speed * 0.8)

    def move_s(self):
        print('move stop')
        self.control.stop()

    def move_r(self):
        print('move right')
        self.control.right(self.speed * 0.8)

    def move_bl(self):
        print('move bottom left')
        self.control.left_motor.forward(self.speed)
        self.control.right_motor.forward(self.speed * 0.8)

    def move_d(self):
        print('move backward')
        self.control.forward(self.speed)

    def move_br(self):
        print('move bottom right')
        self.control.left_motor.forward(self.speed * 0.8)
        self.control.right_motor.forward(self.speed)
    
    def move(self, dir):
        method_name = f'move_{dir}'
        method = getattr(self, method_name)
        method()
