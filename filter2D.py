import numpy as np
import cv2

image = cv2.imread('C:/Users/admin/Downloads/blob1.jpg')
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

p = 0.5
w = int(image.shape[1] * p)
h = int(image.shape[0] * p)
new_img = cv2.resize(image, (w, h))

kernel = np.array([[0.0, -1.0, 0.0],  # create custom kernel here
                   [-1.0, 4.0, -1.0],
                   [0.0, -1.0, 0.0]])

kernel = kernel / (np.sum(kernel) if np.sum(kernel) != 0 else 1)

filty = cv2.filter2D(new_img, -1, kernel)

cv2.imshow("Original", new_img)
cv2.imshow("Filter2D", filty)
cv2.waitKey(0)
cv2.destroyAllWindows()
