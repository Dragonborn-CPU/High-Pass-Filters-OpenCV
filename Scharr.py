import cv2

image = cv2.imread("C:/Users/admin/Downloads/DSC00068.jpg")
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

p = 0.1
w = int(image.shape[1] * p)
h = int(image.shape[0] * p)
new_img = cv2.resize(image, (w, h))

gradients_scharrx = cv2.Scharr(new_img, -1, 1, 0)
gradients_scharry = cv2.Scharr(new_img, -1, 0, 1)
gradients_scharrxy = cv2.addWeighted(gradients_scharrx, 0.5, gradients_scharry, 0.5, 0)

cv2.imshow("Original", new_img)
cv2.imshow("Scharr X", gradients_scharrx)
cv2.imshow("Scharr Y", gradients_scharry)
cv2.imshow("Scharr X+Y", gradients_scharrxy)
cv2.waitKey(0)
cv2.destroyAllWindows()