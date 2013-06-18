import numpy as np
import Metric as me
import Filters as fi

class Lens:
	def __init__(self,lens,metric,bins,debugmode = False):
		self.debugmode = debugmode

		self.lens = lens
		self.metric = metric
		self.bins = bins
		self.filter = fi.Filters(self.lens,self.metric,self.debugmode)
		self.cloud = None
		self.filteredcloud = None
	'''
	filtered  applies filter from Filters.py, sorts on filter variable and places the points into bins.
	'''
	def filtered(self,cloud):
		self.cloud = cloud

		if self.debugmode == True:
			print("In Lens.filtered: The cloud itself:")
			print(self.cloud)

		#filteredcloud is sorted after filter size.
		self.filteredcloud = self.filterpoint()

		if self.debugmode == True:
			print("In Lens.filtered: cloud after filter + sorting")
			print(self.filteredcloud)

		#bins and adds a column of binning data
		self.filteredcloud = self.bins.applybins(self.filteredcloud)
		
		return self.filteredcloud

	#SECTION BELOW TESTED
	'''
	the function filterpoint applies the filter specified as self.lens to each point in the cloud
	'''
	def filterpoint(self):
		
		#creates filter for each point
		self.filteredcloud = self.filter.applyfilter(self.cloud)
		if self.debugmode == True:
			print("In Lens.filterpoint: Cloud after added filthers:")
			print(self.filteredcloud)
		

		#sorts the filtered clouds on filter variable
		temporaryfiltered = np.zeros((self.filteredcloud.shape[0],self.filteredcloud.shape[1]))
		countvar = 0
		for index in np.lexsort((self.filteredcloud[:,0],self.filteredcloud[:,1])):
			temporaryfiltered[countvar] = self.filteredcloud[index,:]
			countvar = countvar+1
		self.filteredcloud = temporaryfiltered
		
		return self.filteredcloud
		
		
