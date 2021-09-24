from gpiozero import MotionSensor
from signal import pause
from datetime import datetime
from picamera import PiCamera
import requests as req
import os
from subprocess import call

camera = PiCamera()
camera.resolution = (640, 480)
camera.rotation = 180

pir = MotionSensor(12)

host = '192.168.117.20'
port = '8000'
url = f'http://{host}:{port}/api/'

video_file_path = ''
start_time = 0

def capture():
    now = datetime.now()
    file_name = now.strftime('%Y%m%d_%H%M%S.jpg')
    file_path = os.path.join('./image', file_name)
    camera.capture(file_path, use_video_port=True)
    print('capture....', file_path)
    return file_path

def upload(url, username, field, file_path, mime):
    data = {
        'username': username,
        'size': os.path.getsize(file_path),
        'filename': os.path.basename(file_path),
        'content_type': mime
    }
    res = req.post(url, data=data, files={
        field: open(file_path, 'br')
    })
    if res.status_code == 200:
        print(res.json())
    else:
        print(res.text)

def upload_snapshot():
    url_snapshot = url + 'snapshot/'
    file_path = capture()
    upload(url_snapshot, 'hong', 'image_file', file_path, 'image/jpeg')

def convert(src, dst):
    command = f"MP4Box -add {src} {dst}"
    call([command], shell=True)

def start_record():
    global video_file_path, start_time
    start_time = datetime.now()
    video_file_name = start_time.strftime('%Y%m%d_%H%M%S.h264')
    video_file_path = os.path.join('video', video_file_name)
    print('start recording...')
    camera.start_recording(video_file_path)

def stop_record():
    camera.stop_recording()
    delta = datetime.now() - start_time
    print(f'end recording (record time : {delta})')

    print('start converting file...')
    mp4_file_path = video_file_path.replace('h264', 'mp4')
    convert(video_file_path, mp4_file_path)
    os.remove(video_file_path)
    print('end converting file and deleting original file')

    url_video = url + 'video/'
    upload(url_video, 'hong', 'video_file', mp4_file_path, 'video/mp4')

def on_motion():
    upload_snapshot()
    start_record()

pir.when_motion = on_motion
pir.when_no_motion = stop_record
pause()
