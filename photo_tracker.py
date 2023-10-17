import os

negative = "cascade_training/negative"
positive = "cascade_training/positive"

type = positive
lines = ""

for i in os.listdir(type):
    try:
        total = len(os.listdir(f"{type}/{i}"))
        if total < 100:
            lines += f"{i}, {total}\n"
    except:
        pass

with open("required_photos.txt", "w") as file:
    file.write(lines)
