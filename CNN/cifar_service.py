import os
import numpy as np
from PIL import Image

from cifar_eval import evaluate


def read_images(image_folder):
    images = []
    excepted = []
    for root, _, files in os.walk(image_folder):
        for f in files:
            excepted.append(int(f.split(".")[0]))
            arr = []
            img = Image.open(os.path.join(root, f)).convert("RGB")
            if img.width != 32 or img.height != 32:
                img = img.resize((32, 32))
            for i in range(32):
                for j in range(32):
                    rgb = img.getpixel((j, i))
                    r = 1.0 - rgb[0] / 255.0
                    g = 1.0 - rgb[1] / 255.0
                    b = 1.0 - rgb[2] / 255.0
                    arr.append(r)
                    arr.append(g)
                    arr.append(b)
            images.append(arr)
    return np.array(images), excepted


if __name__ == "__main__":
    compents = {}
    compents[0] = "air plane"
    compents[1] = "automobile"
    compents[2] = "bird"
    compents[3] = "cat"
    compents[4] = "deer"
    compents[5] = "dog"
    compents[6] = "frog"
    compents[7] = "horse"
    compents[8] = "ship"
    compents[9] = "truck"
    image_folder = "test_images"
    images, excepted = read_images(image_folder)
    predicted = evaluate(images)
    print("\n\n\n---------------------------------------------------------------------")
    print("%16s\t%16s\t%10s" % ("Excepted", "Actually", "Is Right"))
    print("---------------------------------------------------------------------")
    for i in range(len(excepted)):
        print("%16s\t%16s\t%4s" % (
            compents[excepted[i]], compents[predicted[i]],
            "Y" if compents[excepted[i]] == compents[predicted[i]] else "N"))
