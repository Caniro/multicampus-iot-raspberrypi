import cv2

image_file = './data/lena.jpg'
img = cv2.imread(image_file) # cv2.IMREAD_COLOR
img2 = cv2.imread(image_file, cv2.IMREAD_GRAYSCALE)

print(img.shape, img2.shape) # y축, x축, 색상 정보(b, g, r)
cv2.imshow('Lena color', img)
cv2.imshow('Lena grayscale', img2)
cv2.waitKey()
# print(cv2.waitKey(1000))
