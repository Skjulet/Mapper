import os, sys, inspect
import numpy as np
from scipy.spatial import distance
from scipy.cluster.hierarchy import linkage
from scipy.cluster.hierarchy import fcluster

import Mapper as ma
import Lens as le




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
metric = 'cosine'
lens = 'Semantic'
bins = 5
overlap = 0.9
clust = 'CompleteLinkage'
eps = 0.92
testobjekt = ma.Mapper(cloud,metric,lens,bins,overlap,clust,eps,debugmode = False)

testobjekt.addlabels(labeldata)

#testobjekt.visualize()

'''
B = [2,3]
A = np.empty(2)
print(B)
A = np.row_stack((A,B))
print(A)
'''

