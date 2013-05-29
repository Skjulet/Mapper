import numpy as np
import Mapper as ma


cloud = np.ones((2,10))
metric = 'Euclidean'
lens = 'Test'
bins = 3
overlap = 0.1
clust = 'SingleLinkage'
testobjekt = ma.Mapper(cloud,metric,lens,bins,overlap,clust)



