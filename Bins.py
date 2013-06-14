import numpy as np

class Bins:
	def __init__(self,bins = None, overlap = None,equalize = True):
		self.bins = bins
		self.overlap = overlap
		self.equalize = equalize

	def testbins(self, filteredcloud):
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
				if n >= cnt * interval + ol:
					cnt += 1
				if cnt * interval - ol <= n < cnt * interval + ol and cnt < self.bins:	
					#this will never happen
					#if self.overlap == 0:
					#    binningdata[n] = 3				
					#else:
					binningdata[n] = 2
				#moved this before the loop and modified it
				#elif n +1> cnt * interval + ol:
				#    cnt += 1
		
		#A column with bin information is added to filteredcloud
		filteredcloud = np.column_stack((filteredcloud,binningdata))
						

		if self.equalize == False:
			pass
		
		#nagot ska gora med filteredcloud forst :)	
		return filteredcloud

	def applybins(self, filteredcloud):
		'''A method that adds a column to the data with
		information about the bins. The column contains 1's and 2's.
		Were 2's mark overlapping sections of the bins
		'''
		binningdata = np.ones(len(filteredcloud))
		cntboolean = False
		cnt = 1		
		if self.equalize == True:
			interval = len(filteredcloud)/float(self.bins)
			ol = (interval * self.overlap) / 2
			for n in range(len(filteredcloud)):
				if n >= cnt * interval + ol:
					cnt += 1
					cntboolean = True
				if cnt * interval - ol <= n < cnt * interval + ol and cnt < self.bins:	
					binningdata[n] = 2
				if cntboolean == True and binningdata[n] == 2 and binningdata[n-1] == 2:
					binningdata[n] = 4
				if cntboolean == True and binningdata[n] == 1 and binningdata[n-1] == 1:
					binningdata[n] = 3
				cntboolean = False

		if self.equalize == False:
			interval = (max(filteredcloud[:,1])-min(filteredcloud[:,1]))/float(self.bins)
			ol = (interval * self.overlap) / 2
			for n in range(len(filteredcloud)):
				if filteredcloud[n,1] >= cnt * interval + ol:
					cnt += 1
					cntboolean = True
				if cnt * interval - ol <= filteredcloud[n,1] < cnt * interval + ol and cnt < self.bins:	
					binningdata[n] = 2
				if cntboolean == True and binningdata[n] == 2 and binningdata[n-1] == 2:
					binningdata[n] = 4
				if cntboolean == True and binningdata[n] == 1 and binningdata[n-1] == 1:
					binningdata[n] = 3
				cntboolean = False

		#A column with bin information is added to filteredcloud
		filteredcloud = np.column_stack((filteredcloud,binningdata))
		
		return filteredcloud

