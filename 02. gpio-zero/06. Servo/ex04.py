# MQTT 메시지를 subscribe하여 모터 각도 제어
from gpiozero import AngularServo
from time import sleep
import paho.mqtt.client as mqtt

servo = AngularServo(21, min_angle=-90, max_angle=90,
            min_pulse_width=0.00054, max_pulse_width=0.0024)

def setAngle(angle):
    servo.angle = angle

def on_connect (client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    if rc == 0:
        client.subscribe("iot/hong/control/camera")
    else:
        print("연결 실패 : ", rc)

# binary배열.decode() : binary를 문자열로 변환
def on_message(client, userdata, msg):
    value = int(msg.payload.decode())
    print(f"{msg.topic} : {value}")
    setAngle(value)

if __name__ == '__main__':
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message
    try:
        client.connect("192.168.117.20")
        client.loop_forever()
        
    except Exception as e:
        print("에러 :", e)
