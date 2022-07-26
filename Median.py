import cv2

image = cv2.imread("C:/Users/admin/Downloads/DSC00068.JPG")
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

p = 0.1
w = int(image.shape[1] * p)
h = int(image.shape[0] * p)
new_img = cv2.resize(image, (w, h))
cv2.imshow("Original", new_img)

medy = cv2.medianBlur(new_img, 15)
medy1 = new_img - medy + 8

cv2.imshow("Median Filter", medy1)

cv2.waitKey(0)
cv2.destroyAllWindows()
