import numpy as np

class Bins:
	def __init__(self,bins = None, overlap = None,equalize = True):
		self.bins = bins
		self.overlap = overlap
		self.equalize = equalize

	def applybins(self, filteredcloud):
		'''A method that adds a column to the data with
		information about the bins. The column contains 1's and 2's.
		Were 2's mark overlapping sections of the bins
		'''
		binningdata = np.ones(len(filteredcloud))
		if self.equalize == True:
			cnt = 1			
			interval = len(filteredcloud)/float(self.bins)
			ol = (interval * self.overlap) / 2
			for n in range(len(filteredcloud)):
				if cnt * interval - ol <= n < cnt * interval + ol \
				    and cnt < self.bins:	
					if self.overlap == 0:
					    binningdata[n] = 3				
					else:
					    binningdata[n] = 2
				elif n > cnt * interval + ol:
				    cnt += 1
		
		#A column with bin information is added to filteredcloud
		filteredcloud = np.column_stack((filteredcloud,binningdata))
						

		if self.equalize == False:
			pass
		
		#nagot ska gora med filteredcloud forst :)	
		return filteredcloud
