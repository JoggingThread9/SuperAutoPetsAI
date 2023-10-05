# not working currently

import os
import numpy as np
from PIL import Image

# for i in os.listdir("cascade_training"):
#     if i != ".DS_Store":
#         for j in os.listdir(f"cascade_training/{i}"):
#             if j != ".DS_Store":
#                 for k in os.listdir(f"cascade_training/{i}/{j}"):
#                     if k != ".DS_Store":
#                         filePath = f"cascade_training/{i}/{j}/{k}"
#                         file1 = Image.open(f"cascade_training/{i}/{j}/{k}")
#                         file1 = np.array(file1)
#                         for l in os.listdir(f"cascade_training/{i}/{j}"):
#                             if l != ".DS_Store":
#                                 if filePath == f"cascade_training/{i}/{j}/{l}":
#                                     pass
#                                 else:
#                                     file2 = Image.open(f"cascade_training/{i}/{j}/{l}")
#                                     file2 = np.array(file2)
#                                     if np.array_equal(file1, file2):
#                                         os.remove(f"cascade_training/{i}/{j}/{l}")

for i in os.listdir("cascade_training/negative/armadillo"):
    if i != ".DS_Store":
        img1 = np.array(Image.open(f"cascade_training/negative/armadillo/{i}"))
        for j in os.listdir("cascade_training/negative/armadillo"):
            if j != ".DS_Store":
                if i != j:
                    img1 = np.array(Image.open(f"cascade_training/negative/armadillo/{i}"))
                    img2 = np.array(Image.open(f"cascade_training/negative/armadillo/{j}"))
                    if np.array_equal(img1, img2):
                        os.remove(f"cascade_training/negative/armadillo/{j}")

