import cv2

image = cv2.imread("C:/Users/admin/Downloads/DSC00068.jpg")
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

p = 0.1
w = int(image.shape[1] * p)
h = int(image.shape[0] * p)
new_img = cv2.resize(image, (w, h))

img = new_img - cv2.GaussianBlur(new_img, (13, 13), 3) + 8
cv2.imshow('Gaussian Filter', img)
cv2.imshow('Original', new_img)

cv2.waitKey(0)
cv2.destroyAllWindows()
