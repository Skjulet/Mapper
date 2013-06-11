import numpy as np
import Metric as me
import Filters as fi

class Lens:
	def __init__(self,lens,metric,bins):
		self.lens = lens
		self.metric = metric
		self.bins = bins
		self.filter = fi.Filters(self.lens)
		self.cloud = None
		self.filteredcloud = None

	def filtered(self,cloud):
		self.cloud = cloud
		#filteredcloud is sorted after filter size.
		self.filteredcloud = self.filterpoint()

		self.filteredcloud = self.bins.applybins(self.filteredcloud)
		print(self.filteredcloud)
#this function is tested, filter function needed
	def filterpoint(self):

		#cloud.shape gives (x,y) where x is number of rows and y is columns
		self.filteredcloud = np.vstack([range(0,self.cloud.shape[1]), np.zeros(self.cloud.shape[1])])
	

		#insert a filter here
		
		self.filteredcloud = self.filter.applyfilter(self.cloud)

		#ends here

		#sorts the filtered clouds on filter variable
		temporaryfiltered = np.zeros((self.filteredcloud.shape[1],self.filteredcloud.shape[0]))
		countvar = 0
		for index in np.lexsort((self.filteredcloud[0],self.filteredcloud[1])):
			temporaryfiltered[countvar] = self.filteredcloud[:,index]
			countvar = countvar+1
		self.filteredcloud = temporaryfiltered

		return self.filteredcloud
		
	def binning(self):
		pass
	
			
		
		
