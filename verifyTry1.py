import cv2
import os
import sys
import time

UPLOAD_FOLDER = 'image_input'

def mostRecentImage(folder):
    folder = os.path.normpath(folder)
    files = [f for f in os.listdir(folder) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]
    if not files:
        return None

    full_paths = [os.path.normpath(os.path.join(folder, f)) for f in files]

    most_recent_file = max(full_paths, key=os.path.getmtime)
    return most_recent_file

def partQuery():
    chosenPart = ""
    while True:
        chosenPart = input("input part, type h or help \n").lower()

        if chosenPart == 'q':
            sys.exit()
        elif chosenPart == 'h' or chosenPart == 'help':
            print("type q to quit: , avaible options are __, __, __")
        elif chosenPart == 'test':
            chosenPart = "refrence_image/test.jpg"
            break
        #elif chosenPart == 'partName':
        #    chosenPart = "refrence image location"
        else:
            print("Invalid input.")

    return chosenPart


#main
image = cv2.imread(mostRecentImage(UPLOAD_FOLDER))
part = cv2.imread(partQuery(), 0)


#converts target image to grey
grey = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
part = cv2.resize(part, (grey.shape[1] // 2, grey.shape[0] // 2))  # Example resizing

#locate the matching parts
result = cv2.matchTemplate(grey, part, cv2.TM_CCOEFF)
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

print("max_loc: ", max_loc)

cv2.imshow("hi", image)
cv2.imshow("part", part)

cv2.waitKey(0)

cv2.destroyAllWindows()