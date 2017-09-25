import numpy as np

def fun(i):
    return i%4+2

a = np.fromfunction(fun,(10,)) ##10 mean that from 0--9
## the result ::array([ 2.,  3.,  4.,  5.,  2.,  3.,  4.,  5.,  2.,  3.])

