import numpy as np
import Metric as me
from scipy.spatial import distance

class Filters:
	def __init__(self,filtertype,debugmode = False):
		self.filtertype = filtertype

	def applyfilter(self,cloud):
		if self.filtertype == 'Test':
			return np.column_stack((range(0,cloud.shape[0]), np.random.sample(cloud.shape[0])))

		elif self.filtertype == 'Semantic':
			D = distance.squareform(distance.pdist(cloud, metric='cosine'))
			values = np.zeros(len(cloud))
			for n, row in enumerate(D):
			    D[n][row.argmin()]=np.inf
			    iterations = 0
			    while iterations < 6:
				D[n][row.argmin()]=np.inf
				iterations += 1
			    values[n] = D[n][row.argmin()]
			
			return np.column_stack((range(0,cloud.shape[0]), values))
		else:
			pass

