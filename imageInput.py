import os
import sys

UPLOAD_FOLDER = 'image_input'

def mostRecentImage():
    folder = os.path.normpath(UPLOAD_FOLDER)
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
            chosenPart = "refrence_image/testDraw.jpg"
            break
        #elif chosenPart == 'partName':
        #    chosenPart = "refrence image location"
        else:
            print("Invalid input.")

    return chosenPart