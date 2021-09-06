# 이미지 효과 적용
from picamera import PiCamera

camera = PiCamera()

camera.start_preview()

for effect in camera.IMAGE_EFFECTS:
    camera.image_effect = effect
    camera.annotate_text = f'Effect: {effect}'
    camera.capture(f'output/text_{effect}.jpg')

camera.stop_preview()
