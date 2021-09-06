from django.urls import path
from .views import *

urlpatterns = [
    path('', CamView.as_view()),
    path('snapshot/', snapshot, name='snapshot'),
    path('stream/', mjpeg_stream, name='stream'),
]
