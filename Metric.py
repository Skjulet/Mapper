import numpy as np
from scipy.spatial import distance

class Metric:
	def __init__(self,metric,debugmode = False):
		self.metric = metric
		

	def getmetric(self):
		return self.metric
