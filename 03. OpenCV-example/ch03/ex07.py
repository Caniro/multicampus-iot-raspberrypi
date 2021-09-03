# 영상 회전
import cv2

src = cv2.imread('./data/lena.jpg', cv2.IMREAD_GRAYSCALE)

dst1 = cv2.rotate(src, cv2.ROTATE_90_CLOCKWISE)
dst2 = cv2.rotate(src, cv2.ROTATE_90_COUNTERCLOCKWISE)

cv2.imshow('dst1', dst1)
cv2.imshow('dst2', dst2)
cv2.imshow('src', src)

cv2.waitKey()

cv2.destroyAllWindows()
