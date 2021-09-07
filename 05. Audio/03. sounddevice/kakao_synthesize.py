import requests
import io
from pydub import AudioSegment
from pydub.playback import play

URL = "https://kakaoi-newtone-openapi.kakao.com/v1/synthesize"
HEADERS = {
    "Content-Type" : "application/xml",
    "Authorization" : "KakaoAK 3230d1fe69f626c9d5fbb964dc8649c8"
}
DATA = """
<speak>
    그는 그렇게 말했습니다.
    <voice name="MAN_DIALOG_BRIGHT">잘 지냈어? 나도 잘 지냈어.</voice>
    <voice name="WOMAN_DIALOG_BRIGHT" speechStyle="SS_ALT_FAST_1">금요일이 좋아요.</voice>
</speak>
"""

res = requests.post(URL, headers = HEADERS, data = DATA.encode('utf-8'))
if (res.status_code != 200): # 에러 확인
    print(res, res.text)
else:
    # 음성 합성 결과를 파일로 저장하기
    # res.text : 텍스트, res.content : 바이너리
    # with open("result.mp3", "wb") as f:
    #     f.write(res.content)

    # 파일에서 재생
    # song = AudioSegment.from_mp3("./result.mp3")

    # 바로 재생
    # ffmpeg 실행 파일이 환경변수 PATH에 등록되어있어야 한다.
    sound = io.BytesIO(res.content)
    song = AudioSegment.from_mp3(sound)
    play(song)
