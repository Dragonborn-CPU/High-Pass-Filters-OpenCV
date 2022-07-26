import cv2
import numpy as np

image = cv2.imread("C:/Users/admin/Downloads/DSC00068.jpg")
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

p = 0.1
w = int(image.shape[1] * p)
h = int(image.shape[0] * p)
new_img = cv2.resize(image, (w, h))

m = np.array([-1, 2, -1])
g = np.array([-1, 2, -1])

seppy = cv2.sepFilter2D(new_img, -1, m, g)


cv2.imshow("Original", new_img)
cv2.imshow("SepFilter2D", seppy)
cv2.waitKey(0)
cv2.destroyAllWindows()