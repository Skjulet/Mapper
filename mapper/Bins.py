'''A class that adds binning information to the filtered cloud.  
'''


import numpy as np


class Bins:
    def __init__(self, BINNUMBER_int, OVERLAP_flt,
                Equalize_bol, Mother_ma=None):
        
        self.BINNUMBER_int = BINNUMBER_int
        self.OVERLAP_flt = OVERLAP_flt
        self.Equalize_bol = Equalize_bol
        self.DebugMode_bol = Mother_ma.DebugMode_bol

    def apply_bins(self, FilteredPointCloud_npArray):
        '''A method that adds a column to the data with
        information about the bins. The column contains 1's and 2's,
        where 2's mark overlapping sections of the bins.  '''
        
        
        BinningData_npArray = np.ones(len(FilteredPointCloud_npArray))
        
        IntervalSwap_bol = False
        CountInterval_int = 1	
        if self.Equalize_bol == True:
	        BININTERVAL_flt = \
	        len(FilteredPointCloud_npArray)/float(self.BINNUMBER_int)
	        OVERLAPINTERVAL_flt = (BININTERVAL_flt * self.OVERLAP_flt) / 2
	        for Point_int in range(len(FilteredPointCloud_npArray)):
		        if Point_int >= CountInterval_int * BININTERVAL_flt + \
		                                                OVERLAPINTERVAL_flt:
			        CountInterval_int += 1
			        IntervalSwap_bol = True
			    
		        if CountInterval_int * BININTERVAL_flt - OVERLAPINTERVAL_flt \
		        <= Point_int < CountInterval_int * BININTERVAL_flt + \
		        OVERLAPINTERVAL_flt and CountInterval_int < self.BINNUMBER_int:	
			        BinningData_npArray[Point_int] = 2
			    
		        if IntervalSwap_bol == True and BinningData_npArray[Point_int]\
		        == 2 and BinningData_npArray[Point_int-1] == 2:
			        BinningData_npArray[Point_int] = 4
			        
		        if IntervalSwap_bol == True and BinningData_npArray[Point_int]\
		        == 1 and BinningData_npArray[Point_int-1] == 1:
			        BinningData_npArray[Point_int] = 3
		        IntervalSwap_bol = False
		
        #self.Equalize_bol == False needs to be fixed in a later 
        #version.
        SecondIntervalSwap_bol = False
        if self.Equalize_bol == False:
	        BININTERVAL_flt = (max(FilteredPointCloud_npArray[:, 1]) - \
	        min(FilteredPointCloud_npArray[:, 1]))/float(self.BINNUMBER_int)
	        OVERLAPINTERVAL_flt = (BININTERVAL_flt * self.OVERLAP_flt) / 2
	        for Point_int in range(len(FilteredPointCloud_npArray)):
		        if FilteredPointCloud_npArray[Point_int,1] >= \
		        CountInterval_int * BININTERVAL_flt + OVERLAPINTERVAL_flt:
			        while FilteredPointCloud_npArray[Point_int,1] >= \
			        CountInterval_int * BININTERVAL_flt + OVERLAPINTERVAL_flt:
				        CountInterval_int += 1
				        if IntervalSwap_bol == True:
					        SecondIntervalSwap_bol = True
				        IntervalSwap_bol = True
		
		        if CountInterval_int * BININTERVAL_flt - OVERLAPINTERVAL_flt \
		        <= FilteredPointCloud_npArray[Point_int,1] < \
		        CountInterval_int * BININTERVAL_flt + OVERLAPINTERVAL_flt and \
		        CountInterval_int < self.BINNUMBER_int:	
			        BinningData_npArray[Point_int] = 2
			        
		        if IntervalSwap_bol == True and BinningData_npArray[Point_int]\
		        == 2 and BinningData_npArray[Point_int-1] == 2:
			        BinningData_npArray[Point_int] = 4
			        IntervalSwap_bol = False
			        SecondIntervalSwap_bol == False
			        
		        if IntervalSwap_bol == True and BinningData_npArray[Point_int]\
		        == 1 and BinningData_npArray[Point_int-1] == 1:
			        BinningData_npArray[Point_int] = 3
			        IntervalSwap_bol = False
			        SecondIntervalSwap_bol == False

        #A column with bin information is added to 
        #FilteredPointCloud_npArray.
        FilteredPointCloud_npArray = np.column_stack((
                            FilteredPointCloud_npArray, BinningData_npArray))

        return FilteredPointCloud_npArray

