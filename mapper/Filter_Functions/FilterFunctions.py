import numpy as np

class FilterFunctions:
	def __init__(self):
		pass
		
	def gaussian_kde(self, cloud, metric):
		'''
		'''
		from scipy import stats
		kernel = stats.gaussian_kde(cloud.transpose())
		kernel = kernel(cloud.transpose())
		return kernel
	
	def PCA(self, cloud, metric, component=1):
		'''
		'''
		pass
	
	def nth_neighbor(self, cloud, metric):
		'''
		'''
		D = distance.squareform(distance.pdist(cloud, metric=self.metric.getmetric()))
		values = np.zeros(len(cloud))
		for n, row in enumerate(D):
			D[n][row.argmin()]=np.inf
			iterations = 0
			while iterations < 6:
			D[n][row.argmin()]=np.inf
			iterations += 1
			values[n] = D[n][row.argmin()]
