import cv2
import numpy as np

image = cv2.imread("C:/Users/admin/Downloads/DSC00068.jpg")
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

p = 0.1
w = int(image.shape[1] * p)
h = int(image.shape[0] * p)
new_img = cv2.resize(image, (w, h))

kernelX = np.array([[1, 1, 1], [0, 0, 0], [-1, -1, -1]])
kernelY = np.array([[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]])
PrewittX = cv2.filter2D(new_img, -1, kernelX)
PrewittY = cv2.filter2D(new_img, -1, kernelY)

cv2.imshow("Original", new_img)
cv2.imshow("Prewitt", PrewittX + PrewittY)
cv2.waitKey(0)
cv2.destroyAllWindows()