import os
import numpy as np
import cv2
import shutil

for fileName in os.listdir("SAP-pics"):
    if fileName == '.DS_Store':
        continue

    path = f"SAP-pics/{fileName}"

    display = cv2.imread(path)
    display = cv2.resize(display, (1300, 1200))

    display = cv2.cvtColor(display, cv2.COLOR_BGR2RGB)
    display = cv2.cvtColor(display, cv2.COLOR_RGB2BGR)

    cv2.namedWindow("screen")
    cv2.moveWindow("screen", 800, 0)

    cv2.imshow("screen", display)

    cv2.waitKey(1)

    locations = input("Enter Animals:\n")
    locations = locations.split(",")

    for i in range(len(locations)):
        if locations[i][0] == ' ':
            locations[i] = locations[i][1:]

    pets = os.listdir("./cascade_training/positive")

    for i in pets:
        flag = False
        for j in locations:
            if j == i:
                flag = True

        if flag:
            try:
                shutil.copyfile(path, f"cascade_training/positive/{i}/{len(os.listdir(f'''cascade_training/positive/{i}'''))}.png")
            except:
                pass
        else:
            try:
                shutil.copyfile(path, f"cascade_training/negative/{i}/{len(os.listdir(f'''cascade_training/positive/{i}'''))}.png")
            except:
                pass

    shutil.copyfile(path, f"sorted_pics/{len(os.listdir('sorted_pics'))}.png")
    os.remove(path)
    cv2.destroyWindow("screen")
