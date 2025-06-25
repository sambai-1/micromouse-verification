import cv2
import numpy as np

def alignImage(img1, img2):
    gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

    orb = cv2.ORB_create(5000)
    kp1, des1 = orb.detectAndCompute(gray1, None)
    kp2, des2 = orb.detectAndCompute(gray2, None)

    matcher = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
    matches = matcher.match(des1, des2)

    matches = sorted(matches, key=lambda x: x.distance)

    pts1 = [kp1[m.queryIdx].pt for m in matches]
    pts2 = [kp2[m.trainIdx].pt for m in matches]

    H, _ = cv2.findHomography(np.float32(pts2), np.float32(pts1), cv2.RANSAC)

    height, width = img1.shape[:2]
    aligned_img2 = cv2.warpPerspective(img2, H, (width, height))

    return aligned_img2