import argparse
import numpy as np
from scipy import misc
from os import environ
environ['SCIPY_PIL_IMAGE_VIEWER'] = r"C:\WINDOWS\system32\mspaint.exe"

def main(args):
    width = int(args.pixel * args.grid *2)
    data = np.zeros((width, width), dtype=np.uint8)
    for i in range(width):
        grid_number_row = int(np.floor(i / args.pixel))
        for j in range(width):
            grid_number_col = int(np.floor(j / args.pixel))
            if (grid_number_row + grid_number_col) % 2:
                data[i, j] = 255
    misc.imsave(args.output, data)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--pixel", type=int, default=5, help="the number of pixels one edge of one square black or white grid")
    parser.add_argument("-g", "--grid", type=int, default=2, help="the number of grids along one edge")
    parser.add_argument("-o", "--output", type=str, default="checkerboard.png", help="output picture filename")
    args = parser.parse_args()
    main(args)