import numpy as np
import Metric as me

class Lens:
	def __init__(self,lens,metric):
		self.lens = lens
		self.metric = metric
	
	def filtered(self,cloud):
		if self.lens == 'Test':
			length = len(cloud)
			testarray = np.arange(length)
			testarray = 
		else:
			pass
		
		
