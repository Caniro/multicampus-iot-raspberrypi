# PIR 센서로 감지하면 led 불켜고 카카오톡 알림 보내기
from gpiozero import MotionSensor, LED
import requests
import json

pir = MotionSensor(17)
led = LED(27)

def send_talk(message):
    talk_url = "https://kapi.kakao.com/v2/api/talk/memo/default/send"
    with open("access_token.txt", "r") as f:
        token = f.read()
    headers = {"Authorization": f"Bearer {token}"}

    # text_template = {
    #     'object_type': 'text',
    #     'text': message,
    #     'link': {
    #         'web_url': "http://192.168.117.21:8000/mjpeg",
    #         'mobile_web_url': "http://192.168.117.21:8000/mjpeg"
    #     }
    # }
    # print(text_template)
    # payload = {'template_object': json.dumps(text_template)}

    template_object = {
        "object_type": "feed",
        "content": {
            "title": message,
            "description": "침입 발생, 카메라 확인 요망",
            "image_url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcReUAygtoJGju2uhh_REjvtfLe9sdTM71atBw&usqp=CAU",
            "image_width": 640,
            "image_height": 640,
            "link": {
                'web_url': "http://192.168.117.21:8000/mjpeg?mode=stream",
                'mobile_web_url': "http://192.168.117.21:8000/mjpeg?mode=stream",
                "android_execution_params": "contentId=100",
                "ios_execution_params": "contentId=100"
            }
        }
    }
    payload = {'template_object': json.dumps(template_object)}

    res = requests.post(talk_url, data=payload, headers=headers)

def detect():
    led.on()
    send_talk("침입 발생")

pir.when_activated = detect
pir.when_deactivated = led.off
