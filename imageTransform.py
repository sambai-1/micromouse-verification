import numpy as np
import cv2
import imutils
from imutils.perspective import four_point_transform

def transformImage(image):
    #image = cv2.imread(imagePath)
    ratio = image.shape[0] / 500.0
    copy = image.copy() #orig
    image = imutils.resize(image, height = 500)

    #edging
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (5, 5), 0)
    edged = cv2.Canny(gray, 50, 200)

    cv2.imshow("edged", edged)
    countours = cv2.findContours(edged.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    countours = imutils.grab_contours(countours)
    countours = sorted(countours, key = cv2.contourArea, reverse = True)[:5]
    for i in countours:
        peri = cv2.arcLength(i, True)
        approx = cv2.approxPolyDP(i, 0.02 * peri, True)
        if len(approx) == 4:
            screenCnt = approx
            break
        
    cv2.drawContours(image, [screenCnt], -1, (0, 255, 0), 2)
    cv2.imshow("Outline", image)

    warped = four_point_transform(copy, screenCnt.reshape(4, 2) * ratio)
    height, width = warped.shape[:2]

    #used mostly for testPlate only
    if width > height:
        warped = cv2.rotate(warped, cv2.ROTATE_90_CLOCKWISE)
    imutils.resize(warped, height = 650)

    return warped

#transformImage(cv2.imread("refrence_image/testDifference.jpg"))
'''
cv2.imshow("bob", transformImage(cv2.imread("refrence_image/testDraw.jpg")))
cv2.waitKey(0)
cv2.destroyAllWindows'''


#many a thanks to https://pyimagesearch.com/2014/09/01/build-kick-ass-mobile-document-scanner-just-5-minutes/