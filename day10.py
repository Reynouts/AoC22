import numpy as np
import pytesseract
import cv2
from PIL import Image
import matplotlib.pyplot as plt
from scipy.ndimage.filters import gaussian_filter

MARGIN = 100
CONFIG = '--tessdata-dir "C:/Program Files/Tesseract-OCR/tessdata" --psm 10'
pytesseract.pytesseract.tesseract_cmd = "C:/Program Files/Tesseract-OCR/tesseract.exe"


def ocr_pixelchars(arr, image_path='ocr.png'):
    upscaled_image = np.asarray(Image.fromarray(arr).resize([arr.shape[0]*5, arr.shape[1]*5], resample=Image.NEAREST))
    smoothed_image = gaussian_filter(upscaled_image, 1.7)
    plt.imsave(image_path, smoothed_image)
    return pytesseract.image_to_string(cv2.imread(image_path), config=CONFIG)


def string_to_npa(s, target="#", value=1):
    points = set()
    for y, row in enumerate(s.split("\n")):
        for x, c in enumerate(row):
            if c == target:
                points.add((x, y))
    height = max(points,key=lambda item:item[1])[1]+MARGIN+1
    width = max(points,key=lambda item:item[0])[0]+MARGIN+1

    a = np.zeros((height, width))
    for point in points:
        a[point[1]+MARGIN//2, point[0]+MARGIN//2] = value
    return a


def addx(input, parameter):
    return input+parameter, 2


def noop(input, parameter):
    return input, 1


def main():
    with open('day10.txt', 'r') as f:
        instructions = f.read().splitlines()
    ops = {"addx": addx, "noop": noop}
    width = 40
    arg, p_cycle, c_cycle = 1, 1, 1
    result = []
    screen = ""
    for i in instructions:
        i = i.split() + ['0']
        new_arg, s = ops[i[0]](arg, int(i[1]))
        c_cycle += s
        for y in range(p_cycle, c_cycle):
            if (y-1) % width in range(arg-1, arg+2):
                screen += "#"
            else:
                screen += " "
            if y in range(20,221,40):
                result.append(arg*y)
            if y % width == 0:
                screen += "\n"
        arg = new_arg
        p_cycle = c_cycle
    print(f'Part1: {sum(result)}')
    print(f'Part2: {ocr_pixelchars(string_to_npa(screen))}')



if __name__ == "__main__":
    main()