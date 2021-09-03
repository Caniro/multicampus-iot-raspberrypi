# 컬러 변환
import cv2

src = cv2.imread('./data/lena.jpg')
rgb = cv2.cvtColor(src, cv2.COLOR_BGR2RGB) # AI 모듈 : RGB 순서
gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
yCrCv = cv2.cvtColor(src, cv2.COLOR_BGR2YCrCb)
hsv = cv2.cvtColor(src, cv2.COLOR_BGR2HSV)

cv2.imshow('rgb', rgb)
cv2.imshow('gray', gray)
cv2.imshow('yCrCv', yCrCv)
cv2.imshow('hsv', hsv)
cv2.waitKey()
cv2.destroyAllWindows()
