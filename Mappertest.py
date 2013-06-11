import numpy as np
import Mapper as ma
import Lens as le


cloud = np.ones((2,10))
metric = 'Euclidean'
lens = 'Test'
bins = 3
overlap = 0.1
clust = 'SingleLinkage'
testobjekt = ma.Mapper(cloud,metric,lens,bins,overlap,clust)


#print(cloud[:,1], cloud.shape)
#A = np.random.sample(cloud.shape[1])
A = np.vstack([range(0,cloud.shape[1]), np.random.sample(cloud.shape[1])])

#print(A)
#A = np.vstack([np.lexsort((A[0],A[1])),np.lexsort((A[1],A[1]))])
B = np.zeros((cloud.shape[1],cloud.shape[0]))
countvar = 0
for index in np.lexsort((A[0],A[1])):
#	print(index)
	B[countvar] = A[:,index]
	countvar = countvar +1
A = B.transpose()

#print(A) 

a = le.Lens(lens,metric,bins,overlap)

print(a.filterpoint(cloud))


