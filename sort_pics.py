import os
import numpy as np
import cv2
import shutil

for fileName in os.listdir("SAP-pics"):
    if fileName == '.DS_Store':
        break

    path = f"SAP-pics/{fileName}"

    screenshot = cv2.imread(path)
    # screenshot = cv2.resize(screenshot, (1300, 1200))

    screenshot = cv2.cvtColor(screenshot, cv2.COLOR_BGR2RGB)
    screenshot = cv2.cvtColor(screenshot, cv2.COLOR_RGB2BGR)

    cv2.namedWindow("screen")
    # cv2.moveWindow("screen", 700, 0.png)

    cv2.imshow("screen", screenshot)

    cv2.waitKey(1)

    locations = input("Enter Animals:\n")
    locations = locations.split(",")

    for i in range(len(locations)):
        if locations[i][0] == ' ':
            locations[i] = locations[i][1:]

    pets = os.listdir("./cascade_training/positive")

    for i in pets:
        if i in locations:
            try:
                shutil.copyfile(path, f"cascade_training/positive/{i}/{len(os.listdir(f'''cascade_training/positive/{i}'''))}.png")
            except:
                pass
        else:
            try:
                shutil.copyfile(path, f"cascade_training/negative/{i}/{len(os.listdir(f'''cascade_training/negative/{i}'''))}.png")
            except:
                pass

    shutil.copyfile(path, f"sorted_pics/{len(os.listdir('sorted_pics'))}.png")
    os.remove(path)
    cv2.destroyWindow("screen")
