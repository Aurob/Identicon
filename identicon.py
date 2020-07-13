import cv2
import numpy as np
import hashlib
import random

#color sets the default background, default white
def image(width, height, color=255):
    img = np.zeros([width, height, 3], np.uint8)
    img.fill(color)
    return img

#shows numpy image
def show(img, title=""):
    cv2.imshow(title, img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return 1

#hash string (sha256), then convert each character to hex int
def hexhash(string):
    str_hash = hashlib.sha256(string.encode()).hexdigest()
    hex_arr = []
    for ch in str_hash:
        hex_arr.append(ord(ch))
    return hex_arr

#random rgb value
def rand_rgb(seed=0):
    random.seed(seed)
    return [random.randint(0, 256), random.randint(0, 256),random.randint(0, 256)]

#creates a unique visual hash
def icongen(img, hex_arr):
    hex_i = 0
    size = int(img.shape[1]/10)
    seed = int(''.join([str(x) for x in hex_arr]))
    seed_rgb = rand_rgb(seed)
    for x in range(0, img.shape[1], size):
        for y in range(0, img.shape[0], size):
            if hex_arr[hex_i] <= 75:
                img[y:y+size, x:x+size] = seed_rgb
            hex_i+=1
            if hex_i >= len(hex_arr):
                hex_i = 0
    return img

#splits a numpy image in half and mirrors horizontally
def mirror(img, mtype=0):
    height, width, _ = img.shape
    if mtype == 0:
        left_mirror = img[0:height, 0:int(width/2)]
        img[0:height, int(width/2):width] = cv2.flip(left_mirror,1)
    return img

def new_identicon(seed=False):
    if not(seed):
        seed = ''.join([chr(random.randint(51, 101)) for i in range(100)])  
    icon = mirror(icongen(image(100,100), hexhash(seed)))
    return icon

    
