import numpy as np
from sklearn.datasets.samples_generator import make_blobs

def blobs():
    # Generate sample data
    np.random.seed(0)
    batch_size = 45
    centers = [[10, 20], [-10, -10], [17, -10]]
    n_clusters = len(centers)
    X, labels_true = make_blobs(n_samples=40, centers=centers, cluster_std=9)
    np.save('npy_files/example_data_40', X)
    return X


blobs() 	
