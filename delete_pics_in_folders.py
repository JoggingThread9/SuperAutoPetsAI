import os

for i in os.listdir("cascade_training"):
    try:
        for j in os.listdir(f"cascade_training/{i}"):
            try:
                for k in os.listdir(f"cascade_training/{i}/{j}"):
                    try:
                        os.remove(f"cascade_training/{i}/{j}/{k}")
                    except:
                        pass
            except:
                pass
    except:
        pass
