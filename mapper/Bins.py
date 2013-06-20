'''A class that adds binning information to the filtered cloud.  
'''


import numpy as np


class Bins:
    def __init__(self,BINNUMBER_int, OVERLAP_flt,Equalize_bol,DebugMode_bol):

        self.BINNUMBER_int = BINNUMBER_int
        self.OVERLAP_flt = OVERLAP_flt
        self.Equalize_bol = Equalize_bol

    def apply_bins(self, filteredcloud):
        '''A method that adds a column to the data with
        information about the bins. The column contains 1's and 2's,
        where 2's mark overlapping sections of the bins.  '''
        
        
        binningdata = np.ones(len(filteredcloud))
        cntboolean = False
        secondcntboolean = False
        cnt = 1		
        if self.Equalize_bol == True:
	        interval = len(filteredcloud)/float(self.BINNUMBER_int)
	        ol = (interval * self.OVERLAP_flt) / 2
	        for n in range(len(filteredcloud)):
		        if n >= cnt * interval + ol:
			        cnt += 1
			        cntboolean = True
		        if cnt * interval - ol <= n < cnt * interval + ol and cnt < self.BINNUMBER_int:	
			        binningdata[n] = 2
		        if cntboolean == True and binningdata[n] == 2 and binningdata[n-1] == 2:
			        binningdata[n] = 4
		        if cntboolean == True and binningdata[n] == 1 and binningdata[n-1] == 1:
			        binningdata[n] = 3
		        cntboolean = False
        ''' EQUALIZE == FALSE NEEDS TO BE UPGRADED, CASES.  
        '''
        if self.Equalize_bol == False:
	        interval = (max(filteredcloud[:,1])-min(filteredcloud[:,1]))/float(self.BINNUMBER_int)
	        ol = (interval * self.OVERLAP_flt) / 2
	        for n in range(len(filteredcloud)):
		        if filteredcloud[n,1] >= cnt * interval + ol:
			        while filteredcloud[n,1] >= cnt * interval + ol:
				        cnt += 1
				        if cntboolean == True:
					        secondcntboolean = True
				        cntboolean = True
		
		        if cnt * interval - ol <= filteredcloud[n,1] < cnt * interval + ol and cnt < self.BINNUMBER_int:	
			        binningdata[n] = 2
		        if cntboolean == True and binningdata[n] == 2 and binningdata[n-1] == 2:
			        binningdata[n] = 4
			        cntboolean = False
			        secondcntboolean == False
		        if cntboolean == True and binningdata[n] == 1 and binningdata[n-1] == 1:
			        binningdata[n] = 3
			        cntboolean = False
			        secondcntboolean == False

        #A column with bin information is added to filteredcloud
        filteredcloud = np.column_stack((filteredcloud,binningdata))

        return filteredcloud

