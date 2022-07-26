import cv2, numpy as np

image = cv2.imread("C:/Users/admin/Downloads/DSC00070.JPG")
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

p = 0.1
w = int(image.shape[1] * p)
h = int(image.shape[0] * p)
new_img = cv2.resize(image, (w, h))
cv2.imshow("Original", new_img)

# Box Filter
boxy = cv2.boxFilter(new_img, -1, (8, 8))
boxy1 = new_img - boxy + 8  # + 127
# Canny Filter
gradients_canny = cv2.Canny(new_img, 80, 120)  # image1, threshold1, threshold2
# Filter2D
kernel = np.array([[0.0, -1.0, 0.0],  # create custom kernel here
                   [-1.0, 4.0, -1.0],
                   [0.0, -1.0, 0.0]])
kernel = kernel / (np.sum(kernel) if np.sum(kernel) != 0 else 1)
filty = cv2.filter2D(new_img, -1, kernel)
# Gaussian Filter
hpf1 = new_img - cv2.GaussianBlur(new_img, (13, 13), 3) + 8  # height, width, standard dev (set at + 127)
# Laplacian Filter
gradients_laplacian = cv2.Laplacian(new_img, -1)  # src1, ddepth
# LoG Filter
G_Blur = cv2.GaussianBlur(new_img, (5, 5), 0)
LoG_img = cv2.Laplacian(G_Blur, -1)
# Prewitt Filter
kernelX = np.array([[1, 1, 1], [0, 0, 0], [-1, -1, -1]])
kernelY = np.array([[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]])
PrewittX = cv2.filter2D(new_img, -1, kernelX)
PrewittY = cv2.filter2D(new_img, -1, kernelY)
# Scharr Filter
gradients_scharrx = cv2.Scharr(new_img, -1, 1, 0)  # image, ddepth, dx, dy
gradients_scharry = cv2.Scharr(new_img, -1, 0, 1)
gradients_scharrxy = cv2.addWeighted(gradients_scharrx, 0.5, gradients_scharry, 0.5, 0)
# SepFilter
m = np.array([-1, 2, -1])
g = np.array([-1, 2, -1])
seppy = cv2.sepFilter2D(new_img, -1, m, g)
# Sobel Filter
gradients_sobelx = cv2.Sobel(new_img, -1, 1, 0)  # image, ddepth, dx, dy
gradients_sobely = cv2.Sobel(new_img, -1, 0, 1)
gradients_sobelxy = cv2.addWeighted(gradients_sobelx, 0.5, gradients_sobely, 0.5, 0)
# Median Filter
medy = cv2.medianBlur(new_img, 15)
medy1 = new_img - medy + 8
# Bilateral Filter
biby = cv2.bilateralFilter(new_img, 15, 80, 80)
biby1 = new_img - biby + 8

cv2.imshow("Box Filter", boxy1)
cv2.imshow("Canny", gradients_canny)
cv2.imshow("Filter2D", filty)
cv2.imshow("Gaussian Blur", hpf1)
cv2.imshow("Laplacian", gradients_laplacian)
cv2.imshow("Log Gabor", LoG_img)
cv2.imshow("Prewitt", PrewittX + PrewittY)
cv2.imshow("Scharr X+Y", gradients_scharrxy)
cv2.imshow("SepFilter2D", seppy)
cv2.imshow("Sobel X+Y", gradients_sobelxy)
cv2.imshow("Median Blur", medy1)
cv2.imshow("Bilateral Blur", biby1)

cv2.waitKey(0)
cv2.destroyAllWindows()