import os
import numpy as np
from PIL import Image

for i in os.listdir("cascade_training"):
    try:
        for j in os.listdir(f"cascade_training/{i}"):
            try:
                for k in os.listdir(f"cascade_training/{i}/{j}"):
                    try:
                        filePath = f"cascade_training/{i}/{j}/{k}"
                        file1 = Image.open(f"cascade_training/{i}/{j}/{k}")
                        file1 = np.array(file1)
                        for l in os.listdir(f"cascade_training/{i}/{j}"):
                            try:
                                if filePath == f"cascade_training/{i}/{j}/{l}":
                                    pass
                                else:
                                    file2 = Image.open(f"cascade_training/{i}/{j}/{l}")
                                    file2 = np.array(file2)
                                    if np.array_equal(file1, file2):
                                        os.remove(f"cascade_training/{i}/{j}/{l}")
                            except:
                                pass
                    except:
                        pass
            except:
                pass
    except:
        pass