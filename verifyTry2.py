import cv2
import imutils
import numpy as np
from imageTransform import transformImage
from imageInput import partQuery
from imageInput import mostRecentImage


input = cv2.imread(mostRecentImage())
refrence = cv2.imread(partQuery())

inputTransform = transformImage(input)
refrenceTransform = transformImage(refrence)

inputTransform = cv2.resize(inputTransform, (360, 600))
refrenceTransform = cv2.resize(refrenceTransform, (360, 600))

cv2.imshow("bob", inputTransform)
cv2.imshow("bob2", refrenceTransform)

gray1 = cv2.cvtColor(inputTransform, cv2.COLOR_BGR2GRAY)
gray2 = cv2.cvtColor(refrenceTransform, cv2.COLOR_BGR2GRAY)

diff = cv2.absdiff(gray1, gray2)

thresh = cv2.threshold(diff, 0, 100, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
#cv2.imshow("diffs", np.hstack((diff, thresh)))

kernel = np.ones((5, 5), np.uint8)
dilate = cv2.dilate(thresh, kernel, iterations = 2)
#cv2.imshow("bruh", dilate)

countours = cv2.findContours(dilate.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
countours = imutils.grab_contours(countours)

for contour in countours:
    if cv2.contourArea(contour) > 100 and cv2.contourArea(contour) < 1000:

        x, y, w, h = cv2.boundingRect(contour)

        cv2.rectangle(inputTransform, (x, y), (x + w, y + h), (0,0,255), 2)
        cv2.rectangle(refrenceTransform, (x, y), (x + w, y + h), (0,0,255), 2)

cv2.imshow("result", np.hstack((inputTransform, refrenceTransform)))

cv2.waitKey(0)
cv2.destroyAllWindows

#this one thanks to https://youtu.be/Ph4lI-LxzDg?si=pdgzfHszfwo2W66O