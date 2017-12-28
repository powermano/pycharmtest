import numpy as np
import pickle

def channel_wise_mean(data):
    results = []
    shape = data.shape
    assert shape[0] == 1
    sum1 = shape[1]*shape[2]
    for i in range(shape[3]):
        per_layer = data[0,:,:,i]
        results.append(np.sum(per_layer)/sum1)
    return results

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


if __name__=='__main__':
    a={}
    a[123] = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]).reshape((1, 2, 2, 3))
    a[124] = np.array([2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]).reshape((1, 2, 2, 3))
    filepath = 'E:/test.pkl'
    with open(filepath, 'wb') as f:
        pickle.dump(a, f)
    results = load_pkl(filepath)
    print(results)