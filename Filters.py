import numpy as np
import Metric as me

class Filters:
	def __init__(self,filtertype):
		self.filtertype = filtertype

	def applyfilter(self,cloud):
		if self.filtertype == 'Test':
			return np.vstack([range(0,cloud.shape[1]), np.random.sample(cloud.shape[1])])
		else:
			pass

