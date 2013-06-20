'''blobs() function that returns a set of 45 points centered around
given points'''

import numpy as np
from sklearn.datasets.samples_generator import make_blobs

def blobs():
    '''Generates points and writes them to a file
    '''
    # Generate sample data
    np.random.seed(0)
    BatchSize_int = 45
    Centers_array = [[10, 20], [-10, -10], [17, -10]]
    n_clusters = len(Centers_array)
    X, labels_true = make_blobs(n_samples = BatchSize_int, 
                                centers = Centers_array, cluster_std = 9)
    np.save('npy_files/example_data_40', X)
    return X


blobs() 	
