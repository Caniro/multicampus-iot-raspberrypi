from django.contrib.admin.sites import all_sites
from django.urls.conf import path
from .views import *

urlpatterns = [
    path('login/', KakaoLoginView.as_view()),
    path('oauth/', KakaoAuthView.as_view()),
    path('talk/', KakaoTalkView.as_view()),
]
