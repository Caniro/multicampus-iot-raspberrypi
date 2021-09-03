import cv2
import numpy as np
src = cv2.imread('./data/lena.jpg', cv2.IMREAD_GRAYSCALE)
dst = np.zeros(src.shape, dtype=src.dtype)

N = 64 # 가로, 세로 각 N등분
height, width = src.shape
# height, width, _ = src.shape # 컬러일 경우 언팩 시 색상 채널도 받아야 함

h = height // N # 정수 처리
w = width // N

for i in range(N):
    for j in range(N):
        y = i * h
        x = j * w
        roi = src[y:y+h, x:x+w]
        dst[y:y+h, x:x+w] = cv2.mean(roi)[0] # 그레이스케일 영상
        # dst[y:y+h, x:x+w] = cv2.mean(roi)[0:3] # 컬러 영상

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey()
cv2.destroyAllWindows()
