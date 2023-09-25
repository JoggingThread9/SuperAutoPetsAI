import cv2 as cv
import numpy as np
import torch
import io
import os
from PIL import Image
import pyautogui
import PIL.ImageGrab

while True:

    if cv.waitKey(1) == ord('q'):
        cv.destroyAllWindows()
        break
