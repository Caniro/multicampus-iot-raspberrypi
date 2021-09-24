import paho.mqtt.client as mqtt
from . import topicHandler, add_topic_handler
from .devices import move_angle, move_car

def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    if rc == 0:
        client.subscribe('iot/+/control/#')
    else:
        print('connection failed:', rc)
    add_topic_handler('control/camera', move_angle)
    add_topic_handler('control/car', move_car)

def on_message(client, userdata, msg):
    topic = '/'.join(msg.topic.split('/')[2:]) # control/camera
    handler = topicHandler.get(topic)
    if handler:
        value = msg.payload.decode()
        handler(msg.topic, value)
    else:
        print('unknown topic:', msg.topic)

mqttClient = mqtt.Client()
mqttClient.on_connect = on_connect
mqttClient.on_message = on_message

try:
    mqttClient.connect('192.168.117.20')
    mqttClient.loop_start() # 웹서버와는 별도의 스레드로 구동

except Exception as e:
    print('error: ', e)
