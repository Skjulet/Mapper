import numpy as np
from scipy.spatial import distance

class Metric:
	def __init__(self,metric,debugmode = False):
		self.metric = metric
		

	def get_metric(self):
		return self.metric
