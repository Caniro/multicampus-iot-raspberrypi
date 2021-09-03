# 화이트밸런스 조절
from picamera import PiCamera

camera = PiCamera()

camera.start_preview()

for mode in ('auto', 'sunlight', 'off'):
    camera.awb_mode = mode
    camera.capture(f'output/{camera.awb_mode}.jpg')

camera.stop_preview()

# AWB_MODES 값 목록
# off, auto, sunlight, cloudy, shade, tungsten, fluorescent, incandescent,
# flash, horizon
