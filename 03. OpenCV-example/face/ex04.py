# 영상에서 사람 추출
import cv2

body_classifier = cv2.CascadeClassifier('haarcascade_fullbody.xml')

video_file = './data/vtest.avi'
cap = cv2.VideoCapture(video_file)

while True:
    ret, frame = cap.read()
    if ret:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        bodies = body_classifier.detectMultiScale(gray, 1.3, 5)
        for (x, y, w, h) in bodies:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 3)
            cropped_body = frame[y:y+h, x:x+w].copy()
            cropped_body = cv2.resize(cropped_body, dsize=(300, 300),
                            interpolation=cv2.INTER_AREA)

        if 'cropped_body' in locals():
            cv2.imshow('body', cropped_body)
        cv2.imshow('video', frame)

        if cv2.waitKey(1) == 27: break
    else:
        print('error')
        break

if cap.isOpened():
    cap.release()
cv2.destroyAllWindows()
