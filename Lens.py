import numpy as np
import Metric as me

class Lens:
	def __init__(self,lens,metric,bins,overlap):
		self.lens = lens
		self.metric = metric
		self.bins = bins
		self.overlap = overlap
#this function is tested, filter function needed
	def filterpoint(self,cloud):

		#cloud.shape gives (x,y) where x is number of rows and y is columns
		self.filteredcloud = np.vstack([range(0,cloud.shape[1]), np.zeros(cloud.shape[1])])


		#sorts the filtered clouds on filter variable
		temporaryfiltered = np.zeros((self.filteredcloud.shape[1],self.filteredcloud.shape[0]))
		countvar = 0
		for index in np.lexsort((self.filteredcloud[0],self.filteredcloud[1])):
			temporaryfiltered[countvar] = self.filteredcloud[:,index]
			countvar = countvar+1
		self.filteredcloud = temporaryfiltered.transpose()

		return self.filteredcloud
		
	def binning(self):
		pass
	def filtered(self,cloud):
		if self.lens == 'Test':
			length = len(cloud)
			testarray = np.arange(length)
			#testarray = 
		else:
			pass
			
		
		
