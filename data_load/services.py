import requests
import shutil
import requests
from urllib.request import urlopen
from bs4 import BeautifulSoup
import random
import re
from PIL import Image, ImageDraw
import numpy as np


def crop_and_save(array, name):
    l1 = []
    array = array.split(",")
    i = 0
    while i != len(array):
        l1.append((int(array[i]), int(array[i+1])))
        i += 2
    # for i in (0, len(array), 2):
    #     l1.append((int(array[i]), int(array[i+1])))

    print(l1)
    # print(name)
    im = Image.open("media/pics/"+str(name)).convert("RGBA")

    img_array = np.asarray(im)
    # for i in range(0, len(lst)):
    #     l1.append((lst[i]["x"], lst[i]["y"]))
    mask_img = Image.new('L', (img_array.shape[1], img_array.shape[0]), 0)
    ImageDraw.Draw(mask_img).polygon(l1, outline=1, fill=1)
    mask = np.array(mask_img)
    new_img_array = np.empty(img_array.shape, dtype='uint8')
    new_img_array[:, :, :3] = img_array[:, :, :3]
    new_img_array[:, :, 3] = mask*255
    newIm = Image.fromarray(new_img_array, "RGBA")
    newIm.save("media/pics/out.png")
    return "media/pics/out.png"
