from django import forms
import json
import requests

class KakaoTalkForm(forms.Form):
    text = forms.CharField(label="전송할 Talk", max_length=300)
    web_url = forms.CharField(label="Web URL", max_length=300,
                            initial="http://192.168.117.21:8000/mjpeg")
    mobile_web_url = forms.CharField(label="Mobile URL", max_length=300,
                            initial="http://192.168.117.21:8000/mjpeg")

    def send_talk(self):
        talk_url = "https://kapi.kakao.com/v2/api/talk/memo/default/send"
        with open("access_token.txt", "r") as f:
            token = f.read()
        headers = {"Authorization": f"Bearer {token}"}

        text_template = {
            'object_type': 'text',
            'text': self.cleaned_data['text'],
            'link': {
                'web_url': self.cleaned_data['web_url'],
                'mobile_web_url': self.cleaned_data['mobile_web_url']
            }
        }
        print(text_template)
        payload = {'template_object': json.dumps(text_template)}
        res = requests.post(talk_url, data=payload, headers=headers)
        return res, self.cleaned_data['text']
