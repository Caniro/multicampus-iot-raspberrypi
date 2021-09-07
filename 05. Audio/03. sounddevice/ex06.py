# 사용자로부터 입력을 계속 받아서 음성 합성으로 재생
import requests
import io
from pydub import AudioSegment
from pydub.playback import play

URL = "https://kakaoi-newtone-openapi.kakao.com/v1/synthesize"
HEADERS = {
    "Content-Type" : "application/xml",
    "Authorization" : "KakaoAK 3230d1fe69f626c9d5fbb964dc8649c8"
}

voice_list = ("MAN_READ_CALM", "WOMAN_READ_CALM", "MAN_DIALOG_BRIGHT", "WOMAN_DIALOG_BRIGHT")
input_msg = "- 보이스 선택 -\n1: 차분한 남성 낭독체\n2: 차분한 여성 낭독체\n3: 밝은 남성 대화체\n4: 밝은 여성 대화체\n"
voice_num = int(input(input_msg)) - 1
voice_name = voice_list[voice_num]

try:
    while True:
        input_msg = input("음성 합성 문자열 입력 : ")
        DATA = f"""
        <speak>
            <voice name='{voice_name}'>{input_msg}</voice>
        </speak>
        """
        res = requests.post(URL, headers=HEADERS, data=DATA.encode('utf-8'))
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

except KeyboardInterrupt:
    print("\n---입력 종료---")
