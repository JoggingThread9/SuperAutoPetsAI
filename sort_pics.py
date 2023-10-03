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
    # cv2.moveWindow("screen", 700, 0)

    cv2.imshow("screen", screenshot)

    cv2.waitKey(1)

    locations = input("Enter Animals:\n")
    locations = locations.split(" ")

    pets = os.listdir("./cascade_training/positive")

    for i in locations:
        for j in pets:
            if i == j:
                shutil.copyfile(path, f"cascade_training/positive/{i}")
            else:
                shutil.copyfile(path, f"cascade_training/negative/{i}")
    
    cv2.destroyWindow("screen")

    # for pet in pets:
    #     if pet == ".DS_Store":
    #         pass
    #     else:
    #         if pet in names:
    #             num = len(os.listdir(f"cascade_training/positive/{pet}"))
    #             newPath = f"{fileName}({num})"
    #             shutil.copyfile(path, newPath)
    #             shutil.move(newPath, f"cascade_training/positive/{pet}")
    #         else:
    #             num = len(os.listdir(f"cascade_training/negative/{pet}"))
    #             newPath = f"{fileName}({num})"
    #             shutil.copyfile(path, newPath)
    #             shutil.move(newPath, f"cascade_training/negative/{pet}")
    #
    #     os.remove(path)
    # cv2.destroyWindow("screen")
