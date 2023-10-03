import os

folders = os.listdir('pet-icons') + os.listdir('food-icons')

for i in range(len(folders)):
    folders[i] = folders[i].removesuffix('_Icon.png')
    word = ''
    for j in folders[i]:
        j = j.lower()
        word += j
    if '_' in word:
        word = word.replace('_', " ")
    folders[i] = word

for i in folders:
    try:
        os.makedirs(f"cascade_training/positive/{i}")
    except:
        pass

    try:
        os.makedirs(f"cascade_training/positive/frozen {i}")
    except:
        pass

    try:
        os.makedirs(f"cascade_training/negative/{i}")
    except:
        pass

    try:
        os.makedirs(f"cascade_training/negative/frozen {i}")
    except:
        pass
