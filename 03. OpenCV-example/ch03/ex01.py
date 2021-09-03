# 영상 속성
import cv2
import numpy as np

img = cv2.imread('./data/lena.jpg')
# img = cv2.imread('./data/lena.jpg', cv2.IMREAD_GRAYSCALE)
print('img.dmin=', img.ndim)
print('img.shape=', img.shape)
print('img.dtype=', img.dtype)

# np.bool, np.uint16, np.uint32, np.float32, np.float64, np.complex64
img = img.astype(np.int32)
print('img.dtype=', img.dtype)
img = np.uint8(img)
print('img.dtype=', img.dtype)
