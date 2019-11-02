import sys
import json
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from scipy.ndimage import imread
import sys
import statistics

if __name__ == "__main__":
    filename = sys.argv[1]
    data = None
    with open(filename, 'r') as f:
        data = json.load(f)
    times = data["times"]
    median = statistics.median(times)
    std = statistics.stdev(times)
    print("{}: median {}ms, std {}ms".format(data["name"], median, std))