import cv2

class Video:
    def __init__(self, **kargs):
        device = kargs.get('device', -1)
        file = kargs.get('file')
        if device >= 0:
            self.cap = cv2.VideoCapture(device) # 카메라
        elif file:
            self.cap = cv2.VideoCapture(file) # 동영상 파일
    
    def __iter__(self):
        return self

    def __next__(self):
        ret, image = self.cap.read()
        if ret:
            return image
        else:
            raise StopIteration

    def __enter__(self): # Context Manager. with ~ as f 에서 f에 대입할 값을 반환
        return self
    
    def __exit__(self, type, value, trace_back): # Context Manager. with 코드 블록을 벗어날 때 자동으로 호출된다.
        if self.cap and self.cap.isOpened():
            self.cap.release()
        cv2.destroyAllWindows()

    @staticmethod
    def show(image, exit_char=27): # ESC로 종료
        cv2.imshow('frame', image)
        if cv2.waitKey(1) & 0xFF == exit_char:
            return False
        return True

    @staticmethod
    def to_jpg(frame, quality=80):
        encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), quality]
        is_success, jpg = cv2.imencode(".jpg", frame, encode_param)
        return jpg # 거의 성공하므로 성공 여부 체크 안했음

    @staticmethod
    def rescale_frame(frame, percent=75): # 비율로 크기 조정
        width = int(frame.shape[1] * percent / 100)
        height = int(frame.shape[0] * percent / 100)
        dim = (width, height)
        return cv2.resize(frame, dim, interpolation=cv2.INTER_AREA)

    @staticmethod
    def resize_frame(frame, width, height): # 직접 크기 지정해서 조정
        dim = (width, height)
        return cv2.resize(frame, dim, interpolation=cv2.INTER_AREA)

if __name__ == '__main__':
    with Video(device=0) as video:
        for image in video:
            # image = Video.rescale_frame(image, 50)
            print(type(Video.to_jpg(image)))
            if not Video.show(image, ord('q')): break # 문자 to ASCII
