'''
Another clusting method , k-medoids.
See more : http://en.wikipedia.org/wiki/K-medoids
The most common realisation of k-medoid clustering is the Partitioning Around Medoids (PAM) algorithm and is as follows:[2]
1. Initialize: randomly select k of the n data points as the medoids
2. Associate each data point to the closest medoid. ("closest" here is defined using any valid distance metric, most commonly Euclidean distance, Manhattan distance or Minkowski distance)
3. For each medoid m
     For each non-medoid data point o
         Swap m and o and compute the total cost of the configuration
4. Select the configuration with the lowest cost.
5. repeat steps 2 to 4 until there is no change in the medoid.
'''
from clusterBase import importData, pearson_distance, channel_wise_mean, cosine_similarity
import random
import numpy as np

distances_cache = {}

def totalcost(blogwords, costf, medoids_idx):
    size = len(blogwords)
    total_cost = 0.0
    medoids = {}
    for idx in medoids_idx:
        medoids[idx] = []
    for i in range(size):
        choice = None
        min_cost = np.inf
        for m in medoids:
            tmp = distances_cache.get((m, i), None)
            if tmp == None:
                tmp = pearson_distance(blogwords[m, :], blogwords[i, :])
                distances_cache[(m, i)] = tmp
            if tmp < min_cost:
                choice = m
                min_cost = tmp
        medoids[choice].append(i)
        total_cost += min_cost
    return total_cost, medoids


def kmedoids(blogwords, k):
    size = len(blogwords)
    medoids_idx = random.sample([i for i in range(size)], k)
    pre_cost, medoids = totalcost(blogwords, pearson_distance, medoids_idx)
    print (pre_cost)
    current_cost = np.inf  # maxmum of pearson_distances is 2.
    best_choice = []
    best_res = {}
    iter_count = 0
    while 1:
        for m in medoids:
            for item in medoids[m]:
                if item != m:
                    idx = medoids_idx.index(m)
                    swap_temp = medoids_idx[idx]
                    medoids_idx[idx] = item
                    tmp, medoids_ = totalcost(blogwords, pearson_distance, medoids_idx)
                    # print tmp,'-------->',medoids_.keys()
                    if tmp < current_cost:
                        best_choice = list(medoids_idx)
                        best_res = dict(medoids_)
                        current_cost = tmp
                    medoids_idx[idx] = swap_temp
        iter_count += 1
        print(current_cost, iter_count)
        if best_choice == medoids_idx: break
        # if iter_count == 1: break
        if current_cost <= pre_cost:
            pre_cost = current_cost
            medoids = best_res
            medoids_idx = best_choice

    return current_cost, best_choice, best_res


def show(dataSet, k, centroids, clusterAssment):
    from matplotlib import pyplot as plt
    numSamples, dim = dataSet.shape
    mark =  ['or', 'ob', 'og', 'ok', '^r', '+r', 'sr', 'dr', '<r', 'pr', 'xr', 'sb', 'sg', 'sk', '2r', '<b', '<g', '+b', '+g', 'pb']
    # for i in range(numSamples):
        # markIndex = int(clusterAssment[i, 0])
        # for j in range(len(clusterAssment)):
        #     if i in clusterAssment[clusterAssment.keys()[j]]:
        #         plt.plot(dataSet[i, 0], dataSet[i, 1], mark[j])
    count = 0
    for item in clusterAssment:
        for i in clusterAssment[item]:
            plt.plot(dataSet[i, 0], dataSet[i, 1], mark[count])
        count += 1

    #mark = ['Dr', 'Db', 'Dg', 'Dk', '^b', '+b', 'sb', 'db', '<b', 'pb', 'or', 'ob', 'og', 'ok', '^r', '+r', 'sr', 'dr', '<r', 'pr']
    #for i in range(k):
        #plt.plot(centroids[i][0, 0], centroids[i][0, 1], mark[i], markersize=12)
    plt.show()


def getDataset(filename, k_sample):
    import linecache
    import random
    dataMat = []
    myfile = open(filename)
    lines = len(myfile.readlines())
    SampleLine = random.sample([i for i in range(lines)], k_sample)
    for i in SampleLine:
        theline = linecache.getline(filename, i)
        curLine = theline.strip().split()
        fltLine = map(float, curLine)  # transfer to float
        dataMat.append(fltLine)
    return dataMat

# load example
def load_data(filename):
    dataset = []
    count = 1
    with open(filename) as f:
        datalines = f.readlines()
    for item in datalines:
        example = item.strip().split()
        data = np.array([float(x) for x in example]) # x is string
        if count == 1:
            dataset = data
        else:
            dataset = np.vstack((dataset, data))
        count += 1
    return dataset

# load pkl.example
uncertainty_file = 'E:/'
def load_pkl(filename):
    import pickle
    result = []
    count = 1
    with open(filename, 'rb') as f:
        data_dict = pickle.load(f)
    for item in data_dict:
        if count == 1:
            temp = channel_wise_mean(data_dict[item])
            result1 = [item]
            result1.extend(temp)
            result = np.array([result1])
        else:
            temp = channel_wise_mean(data_dict[item])
            result1 = [item]
            result1.extend(temp)
            result = np.vstack((result, np.array([result1])))
        count += 1
    return  result

f_measure = {} # for store the similarity computation, so as to avoid duplicate computation
def f(sa, x, result):
    """

    :param sa: a list of index, type:int
    :param x:  a index, type; int
    :param result: a np.array : [index ,x1, x2,...xn]
    :return: the max_similarity between sa and x
    """
    assert len(sa) > 0
    max_similarity = -np.inf
    for i in range(len(sa)):
        temp = f_measure.get((sa[i], x), None)
        if temp == None:
            temp = cosine_similarity(result[sa[i], 1:], result[x, 1:])
        if temp > max_similarity:
            max_similarity = temp
    return max_similarity

def F(sa, su, result):
    all_similarity = 0
    for i in range(len(su)):
        all_similarity += f(sa, su[i], result)
    return all_similarity

def greedy_search(sa, sc, su, k, result):
    pass

if __name__ == '__main__':
    # dataMat = getDataset('R15.txt',150)
    # best_cost, best_choice, best_medoids = kmedoids(dataMat, 15)
    # dataMat = mat(dataMat)
    # listone = []
    # for i in range(len(best_choice)):
    #     listone.append(dataMat[best_choice[i]])
    # show(dataMat, 15, listone, best_medoids)
    filepath = r'E:/test.txt'
    dataset = load_data(filepath)
    best_cost, best_choice, best_medoids = kmedoids(dataset, 2)
    for i in best_medoids:
        print(i, best_medoids[i])
    listone =[]
    for i in range(len(best_choice)):
        listone.append(dataset[best_choice[i]])
    show(dataset, 2, listone, best_medoids)


