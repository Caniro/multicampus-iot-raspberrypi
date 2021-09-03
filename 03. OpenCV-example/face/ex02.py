# 이미지 모자이크
import cv2

cascade_file = "haarcascade_frontalface_default.xml"
cascade = cv2.CascadeClassifier(cascade_file)

# image_file = './data/face1.jpg'
image_file = './data/face2.jpg'

image = cv2.imread(image_file)
image_gs = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
face_list = cascade.detectMultiScale(image_gs, scaleFactor=1.1,
                            minNeighbors=1, minSize=(100, 100))

if len(face_list) == 0:
    print("No face")
    quit()

mosaic_rate = 20

print(face_list)
color = (0, 0, 255)

for (x, y, w, h) in face_list:
    face_img = image[y:y+h, x:x+w]
    face_img = cv2.resize(face_img, (w//mosaic_rate, h//mosaic_rate))
    face_img = cv2.resize(face_img, (w, h), 
                    interpolation=cv2.INTER_AREA) # 같은 색으로 채우기
    image[y:y+h, x:x+w] = face_img

cv2.imshow("image", image)
cv2.waitKey()
cv2.destroyAllWindows()
