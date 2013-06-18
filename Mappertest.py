import numpy as np
import Mapper as ma
import Lens as le
from scipy.spatial import distance
from scipy.cluster.hierarchy import linkage
from scipy.cluster.hierarchy import fcluster

def SLcluster(data,eps):
    X = data
    
    Y = distance.pdist(X, metric='euclidean')
    Y = Y / np.max(Y)
    Y[Y<0] = 0
    
    Z = linkage(Y,'complete')
    
    labels = fcluster(Z,t=eps,criterion='distance')
    
    return labels



worddata = np.load('npy_files/easygoing_neighbors.npy')
labeldata = np.load('npy_files/easygoing_neighborswords.npy')
cloud = worddata
metric = 'Euclidean'
lens = 'Semantic'
bins = 5
overlap = 0.9
clust = 'CompleteLinkage'
eps = 0.92
testobjekt = ma.Mapper(cloud,metric,lens,bins,overlap,clust,eps,debugmode = False)



testobjekt.addlabels(labeldata)


testobjekt.visualize()


