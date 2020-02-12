import sys
import json
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from imageio import imwrite
from os import environ
environ['SCIPY_PIL_IMAGE_VIEWER'] = r"C:\WINDOWS\system32\mspaint.exe"

def oned_to_2d_coord(oned, col_max):
    row = int(oned / col_max)
    col = oned % col_max
    return row, col

def recovery(data):
    dim = data["dim"]
    row_max = dim[0]
    col_max = dim[1]
    name = data["name"]
    times = np.array(data["times"], dtype=np.float32)
    data_mat = times.reshape(row_max, col_max)
    kmeans = KMeans(n_clusters=2, random_state=0).fit(times.reshape(-1, 1))
    label_to_color = {0: 0, 1: 1}
    print(kmeans.cluster_centers_)
    if kmeans.cluster_centers_[0, 0] > kmeans.cluster_centers_[1, 0]:
        label_to_color = {0: 1, 1: 0}
    image = np.zeros((row_max, col_max), dtype=np.uint8)
    for i in range(col_max*row_max):
        label = kmeans.labels_[i]
        row, col = oned_to_2d_coord(i, col_max)
        color = label_to_color[label]
        image[row, col] = color*255
    imwrite("{}_recover.png".format(name), image)
    fig, ax = plt.subplots()
    im = ax.imshow(data_mat, cmap=plt.cm.gray)
    for row in range(row_max):
        for col in range(col_max):
            text = ax.text(col, row, int(data_mat[row, col]),
                       ha="center", va="center", color="w")
    fig.tight_layout()
    plt.colorbar(im);
    #plt.show()
    plt.savefig("{}_heatmap.png".format(name))


if __name__ == "__main__":
    filename = "post_body.json"
    if len(sys.argv) > 1:
        filename = sys.argv[1]
    data = None
    with open(filename, 'r') as post_body:
        data = json.load(post_body)
    recovery(data)