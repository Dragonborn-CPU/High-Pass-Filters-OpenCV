import cv2

image = cv2.imread("C:/Users/admin/Downloads/DSC00068.jpg")
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

p = 0.1
w = int(image.shape[1] * p)
h = int(image.shape[0] * p)
new_img = cv2.resize(image, (w, h))

gradients_sobelx = cv2.Sobel(new_img, -1, 1, 0)
gradients_sobely = cv2.Sobel(new_img, -1, 0, 1)
gradients_sobelxy = cv2.addWeighted(gradients_sobelx, 0.5, gradients_sobely, 0.5, 0)

cv2.imshow("Original", new_img)
cv2.imshow("Sobel X", gradients_sobelx)
cv2.imshow("Sobel Y", gradients_sobely)
cv2.imshow("Sobel X+Y", gradients_sobelxy)
cv2.waitKey(0)
cv2.destroyAllWindows()