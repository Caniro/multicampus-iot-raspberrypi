# BGR 형식의 unencoded numpy 배열로 저장
from picamera import PiCamera
import numpy as np
import cv2

with PiCamera() as camera:
    x, y = (640, 480)
    camera.resolution = (x, y)
    camera.framerate = 24

    # 1차원 배열로 초기화
    image = np.empty((x * y * 3, ), dtype=np.uint8)
    print(image.shape)
    camera.capture(image, 'bgr')
    # 3차원 numpy 배열로 재구성, y축이 먼저 나와야 한다.
    image = image.reshape((y, x, 3))
    print(image.shape)

    # 아니면 바로 3차원 배열로 초기화해도 된다.
    # image = np.empty((y, x, 3), dtype=np.uint8)

    while True:
        # camera.capture(image, 'bgr') # 소프트웨어적인 캡처. 품질 좋은데 느림
        # 하드웨어 인코더 사용 -> 빠르지만 품질은 낮음
        camera.capture(image, 'bgr', use_video_port=True)
        cv2.imshow('frame', image)
        if cv2.waitKey(1) == 27: # ESC
            break
