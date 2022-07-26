import cv2

image = cv2.imread("C:/Users/admin/Downloads/blob1.jpg")
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

p = 0.5
w = int(image.shape[1] * p)
h = int(image.shape[0] * p)
new_img = cv2.resize(image, (w, h))

G_Blur = cv2.GaussianBlur(new_img, (5, 5), 0)
LoG_img = cv2.Laplacian(G_Blur, -1)

cv2.imshow("Original", new_img)
cv2.imshow("Log Gabor", LoG_img)
cv2.waitKey(0)
cv2.destroyAllWindows()