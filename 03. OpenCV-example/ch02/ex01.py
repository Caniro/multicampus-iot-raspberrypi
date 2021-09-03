# 직선, 사각형 그리기
import numpy as np
import cv2

#모두 0으로 되어 있는 빈 Canvas(검정색)
img = np.zeros((512, 512, 3), np.uint8)
cv2.line(img, (0, 0), (511, 511), (255, 0, 0), 5)
cv2.rectangle(img, (384, 0), (510, 128), (0,255,0), 3)

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
