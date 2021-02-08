import pytesseract
import cv2
import numpy as np
from os import listdir
from os.path import isfile, join
from win32.win32api import GetSystemMetrics

width = GetSystemMetrics(0)
height = GetSystemMetrics(1)


def show_box(img, name):
    val_lst = list(img.shape)
    boxes = pytesseract.image_to_boxes(img)
    for b in boxes.splitlines():
        b = b.split(' ')
        img = cv2.rectangle(img, (int(b[1]), val_lst[0]-int(b[2])), (int(b[3]), val_lst[0]-int(b[4])), (0, 255, 0), 2)
    img = cv2.resize(img, (width, height))
    cv2.imshow('img', img)
    if cv2.waitKey(0) == ord('q'):
        cv2.destroyAllWindows()

def ocr_core(image):
    text = pytesseract.image_to_string(image)
    return text

def find_path():
    test_image_names = [f for f in listdir("test_images") if isfile(join("test_images", f))]
    return test_image_names
