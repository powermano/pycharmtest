from math import sqrt
from scipy.spatial.distance import pdist
import numpy as np

def importData(fileName) :
    dataMat = []
    with open(fileName) as f:
        for line in f.readlines():
            curLine = line.strip().split()
            fltLine = map(float, curLine)  # transfer to float
            dataMat.append(fltLine)
    return dataMat


def pearson_distance(vector1, vector2) :
    """
    Calculate distance between two vectors using l2
    See more : http://en.wikipedia.org/wiki/Pearson_product-moment_correlation_coefficient
    """
    X = np.vstack([vector1, vector2])
    d2 = pdist(X)
    return d2

def cosine_similarity(vertor1, vertor2):
    """
    calculate similarity between two vertors using cosine measuring
    :param vertor1:  numpy  type
    :param vertor2:  numpy  type
    :return: cosine similarity
    """
    total = np.sum(vertor1 * vertor2)
    v1 = np.sqrt(np.sum(vertor1 * vertor1))
    v2 = np.sqrt(np.sum(vertor2 * vertor2))
    return total/(v1*v2)

def channel_wise_mean(data):
    results = []
    shape = data.shape
    assert shape[0] == 1
    sum1 = shape[1]*shape[2]
    for i in range(shape[3]):
        per_layer = data[0,:,:,i]
        results.append(np.sum(per_layer)/sum1)
    return results