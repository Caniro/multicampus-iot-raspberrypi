from gpiozero import MotionSensor
from signal import pause
from datetime import datetime
from picamera import PiCamera
import requests as req
import os

camera = PiCamera()
camera.resolution = (640, 480)
camera.rotation = 180

pir = MotionSensor(12)

url = 'http://192.168.117.20:8000/api/snapshot/'

def capture():
    now = datetime.now()
    file_name = now.strftime('%Y%m%d_%H%M%S.jpg')
    file_path = os.path.join('./images', file_name)
    camera.capture(file_path, use_video_port=True)
    print('capture....', file_path)
    return file_name, file_path

def upload_snapshot():
    file_name, file_path = capture()
    data = {
        'username': 'hong',
        'size': os.path.getsize(file_path),
        'filename': file_name,
        'content_type': 'image/jpeg'
    }
    res = req.post(url, data=data, files={
        'image_file': open(file_path, 'br')
    })
    if res.status_code == 200:
        print(res.json())
    else:
        print(res.text)

pir.when_motion = upload_snapshot
pause()
