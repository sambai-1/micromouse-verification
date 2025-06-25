import cv2
import numpy as np
from imageAlign import alignImage
from imageDetect import findDifference
from skimage.metrics import structural_similarity as ssim

# Load and align images
img1 = cv2.imread("./image_input/inputDifference.png")
img2 = cv2.imread("./refrence_image/testDifference.jpg")
img2 = alignImage(img1, img2)

gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

score, difference = ssim(gray1, gray2, full=True)
difference = (1 - difference) * 255
difference = difference.astype("uint8")

_, thresh = cv2.threshold(difference, 200, 255, cv2.THRESH_BINARY)

kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
difference = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel)

cv2.imshow("Difference", difference)

side = 70
x, y = findDifference(side, difference)
half = side // 2
topLeft = (x - half, y - half)
botRight = (x + half, y + half)
cv2.rectangle(img1, topLeft, botRight, (0, 0, 255), 2)

# Show the result
cv2.imshow("Original with Difference Circle", img1)
cv2.waitKey(0)
cv2.destroyAllWindows()


cv2.waitKey(0)

