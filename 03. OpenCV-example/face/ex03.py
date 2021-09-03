# 카메라 영상에서 얼굴 영역 추출
import cv2

face_classifier = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture(0)

if cap.isOpened():
    print(f'width: {cap.get(3)}, height: {cap.get(4)}')
else:
    print("No Camera")

while True:
    ret, frame = cap.read()
    if ret:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_classifier.detectMultiScale(gray, 1.3, 5)
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 3)
            cropped_face = frame[y:y+h, x:x+w].copy()
            cropped_face = cv2.resize(cropped_face, dsize=(300, 300),
                            interpolation=cv2.INTER_AREA)

        if 'cropped_face' in locals():
            cv2.imshow('face', cropped_face)
        cv2.imshow('video', frame)

        if cv2.waitKey(30) == 27: break
    else:
        print('error')

cap.release()
cv2.destroyAllWindows()
