from PIL import Image
from PIL import ImageFilter


def applyMinimumFilter(image):
    return image.filter(ImageFilter.MinFilter)


imagePath = "C:/Users/admin/Downloads/DSC00068.JPG"
imageObject = Image.open(imagePath)

filterApplied = imageObject
for i in range(0, 25):
    filterApplied = applyMinimumFilter(filterApplied)

imageObject.show()
filterApplied.show()
