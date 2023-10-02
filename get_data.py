# not working for mac as key presses do not track across windows

import cv2 as cv
from PIL import ImageGrab
import os
import pygame
import numpy as np

pygame.init()

run = True

name = os.listdir("SAP-pics")
while run:
    screenshot = ImageGrab.grab()
    screenshot = np.array(screenshot)
    screenshot = cv.cvtColor(screenshot, cv.COLOR_BGR2RGB)

    cv.imshow("window", screenshot)

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
            if event.key == pygame.K_q:
                run = False
            elif event.key == pygame.K_p:
                name = os.listdir("SAP-pics")
                name = len(name)
                cv.imwrite(f"SAP-pics/{name}.png", screenshot)