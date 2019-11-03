import sys
import json
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from scipy.ndimage import imread
import argparse

def read_img(filename):
    gray = imread(fname=filename, mode='L')
    bw = gray > 70
    return bw

def main(args):
    groundtruth = read_img(args.groundtruth)
    recovered = read_img(args.recovered)
    rows, cols = groundtruth.shape
    if args.inverse:
        recovered = np.logical_not(recovered)
    error_white = 0
    error_black = 0
    for i in range(rows):
        for j in range(cols):
            if groundtruth[i, j] != recovered[i, j]:
                if groundtruth[i, j]:
                    error_white += 1
                else:
                    error_black += 1
    print("error black pixels: {}; error white pixels: {}".format(error_black, error_white))

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-g", "--groundtruth", type=str, default="checkerboard.png", help="the ground truth image")
    parser.add_argument("-r", "--recovered", type=str, help="the recovered image")
    parser.add_argument("-i", "--inverse", action="store_true", help="inversed black and white")
    args = parser.parse_args()
    main(args)
    