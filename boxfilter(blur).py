import cv2

image = cv2.imread("C:/Users/admin/Downloads/DSC00068.jpg")
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

p = 0.1
w = int(image.shape[1] * p)
h = int(image.shape[0] * p)
new_img = cv2.resize(image, (w, h))
cv2.imshow("Original", new_img)

boxy = cv2.boxFilter(new_img, -1, (8, 8))  # ddepth, ksize (8, 8)
boxy1 = new_img - boxy + 8

cv2.imshow("Box Filter as High Pass", boxy1)

cv2.waitKey(0)
cv2.destroyAllWindows()
