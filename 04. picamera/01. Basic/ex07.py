# 노출 조절
from picamera import PiCamera

camera = PiCamera()

camera.start_preview()

for mode in ('beach', 'night', 'snow', 'fireworks'):
    camera.exposure_mode = mode
    camera.hflip = True
    camera.vflip = True
    camera.capture(f'output/{camera.exposure_mode}.jpg')

camera.stop_preview()

# EXPOSURE_MODES 값 목록
# off, auto, night, nightpreview, backlight, spotlight, sports, snow, beach,
# verylong, fixedfps, antishake, fireworks
