import os
from django.http.response import HttpResponse, StreamingHttpResponse
from django.views.generic import TemplateView
from time import sleep
from datetime import datetime
from mysite.picam import MJpegStreamCam
from mysite.settings import BASE_DIR

SNAPSHOT_DIR = os.path.join(BASE_DIR, 'media/snapshot/')

mjpegstream = MJpegStreamCam()

def get_snapshot_history():
    files = os.listdir(SNAPSHOT_DIR)
    files.sort(reverse=True)
    return files

class CamView(TemplateView):
    template_name = "cam.html"

    def get_context_data(self):
        context = super().get_context_data()
        context["mode"] = self.request.GET.get("mode", "#")
        context["snapshot_history"] = get_snapshot_history()
        return context

def save_image(image):
    now = datetime.now()
    fname = now.strftime("snapshot_%Y%m%d_%H%M%S.jpg")
    file_path = os.path.join(SNAPSHOT_DIR, fname)
    print(file_path)
    with open(file_path, "wb") as f:
        f.write(image)

def snapshot(request):
    sleep(0.3) # 이전 작업의 cleanup 대기 (없으면 stream -> snapshot 이동 시 오류)
    image = mjpegstream.snapshot()
    save_image(image)
    return HttpResponse(image, content_type="image/jpeg")

def mjpeg_stream(request):
    # 아래 객체가 mjpegstream에서 계속 yield를 받아서 스트리밍한다.
    return StreamingHttpResponse(mjpegstream,
        content_type='multipart/x-mixed-replace;boundary=--myboundary')
