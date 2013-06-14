import numpy as np
import Mapper as ma
import Lens as le

	
cloud = np.ones((2,20))
metric = 'Euclidean'
lens = 'Test'
bins = 5
overlap = 0.5
clust = 'SingleLinkage'
testobjekt = ma.Mapper(cloud,metric,lens,bins,overlap,clust,debugmode = True)


#print(cloud[:,1], cloud.shape)
A = np.random.sample(cloud.shape[1])
A = np.vstack([range(0,cloud.shape[1]), np.random.sample(cloud.shape[1])])


#print(max(A[1,:])) 
#print(A[1,:]) 

'''a = (1,2)
print(a)
print(a[1])
'''

