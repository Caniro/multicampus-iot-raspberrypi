from django.shortcuts import render
from django.views.generic import TemplateView, FormView
import json
import requests
from django.contrib import messages
from .secret_config import client_id
from .forms import KakaoTalkForm
# import mjpeg.sensors

class KakaoLoginView(TemplateView):
    template_name = "kakao_login.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["client_id"] = client_id
        return context

class KakaoAuthView(TemplateView):
    template_name = "kakao_token.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        code = self.request.GET['code']
        token = self.getAccessToken(code)
        context["client_id"] = client_id
        context["token"] = token
        self.save_access_token(token["access_token"])
        return context

    def getAccessToken(self, code):
        url = "https://kauth.kakao.com/oauth/token"

        headers = {
            "Content-Type": "application/x-www-form-urlencoded", # 키=값&키=값&... 형식으로 전송
            "Cache-Control": "no-cache"
        }

        payload = "grant_type=authorization_code"
        payload += "&client_id=" + client_id
        payload += "&redirect_url=http://192.168.117.21:8000/kakao/oauth&code=" + code

        response = requests.post(url, data=payload, headers=headers)
        return response.json()

    def save_access_token(self, access_token):
        with open("access_token.txt", "w") as f:
            f.write(access_token)

class KakaoTalkView(FormView):
    form_class = KakaoTalkForm
    template_name = "kakao_form.html"
    success_url = "/kakao/talk"

    def form_valid(self, form):
        res, text = form.send_talk()
        if res.json().get('result_code') == 0:
            messages.add_message(self.request, messages.SUCCESS,
                            "메시지 전송 성공 : " + text)
        else:
            messages.add_message(self.request, messages.ERROR,
                            "메시지 전송 실패 : " + str(res.json()))
        return super().form_valid(form)
