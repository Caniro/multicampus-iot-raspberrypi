from io import BytesIO
from picamera import PiCamera

class PiCam:
    def __init__(self, framerate=25, width=640, height=480):
        self.size = (width, height)
        self.framerate = framerate

        self.camera = PiCamera()
        self.camera.rotation = 180
        self.camera.resolution = self.size
        self.camera.framerate = self.framerate

    def snapshot(self):             # 사진 1장 jpeg 캡처해서 리턴
        frame = BytesIO()
        self.camera.capture(frame, 'jpeg', use_video_port=True)
        frame.seek(0)
        # return frame.read()     # 바이트 배열 리턴
        return frame.getvalue()     # 바이트 배열 리턴

class MJpegStreamCam(PiCam):
    def __init__(self, framerate=25, width=640, height=480):
        super().__init__(framerate=framerate, width=width, height=height)

    def __iter__(self):
        frame = BytesIO()
        while True:
            self.camera.capture(frame, format="jpeg", use_video_port=True)
            image = frame.getvalue()
            yield (b'--myboundary\n'
                    b'Content-Type:image/jpeg\n'
                    b'Content-Length: ' + f"{len(image)}".encode() + b'\n\n' +
                    image + b'\n')
            frame.seek(0)
            frame.truncate() # 현재 위치에서 뒷 부분(기존 데이터) 제거
