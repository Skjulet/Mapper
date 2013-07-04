'''A class that adds binning information to the filtered point cloud.
'''


import numpy as np


class Bins:
    def __init__(self, BINNUMBER_int, OVERLAP_flt,
                Equalize_bol, Mother_ma=None):
        '''A class that adds  binning information to the filtered point
        cloud.  '''
        
        self.BINNUMBER_int = BINNUMBER_int
        self.OVERLAP_flt = OVERLAP_flt
        self.Equalize_bol = Equalize_bol
        self.DebugMode_bol = Mother_ma.DebugMode_bol
     
    def apply_bins(self, FilteredPointCloud_npArray):
        '''A method that creates an array with binning information.
        Each element in the array is a bin contatining points.  '''
        
        
        Binning_npArray = []
        
        CountInterval_int = 1	
        if self.Equalize_bol == True:
            PointsToCheck_array = range(len(FilteredPointCloud_npArray))
            BININTERVAL_flt = \
                len(FilteredPointCloud_npArray)/float(self.BINNUMBER_int)
        else:
            PointsToCheck_array = FilteredPointCloud_npArray[:,1]
            BININTERVAL_flt = \
                len(FilteredPointCloud_npArray)/float(self.BINNUMBER_int)
        #print(FilteredPointCloud_npArray[:,1],
        #FilteredPointCloud_npArray[:,1][-1], 
        #FilteredPointCloud_npArray[:,1][0])
        
        OVERLAPINTERVAL_flt = (BININTERVAL_flt * self.OVERLAP_flt) / 2
        
        Point_int = 0
        CurrentBin_int = 1
        CurrentBin_array = []
        Overlap_array = []
        while Point_int < len(FilteredPointCloud_npArray):
            if (CurrentBin_int - 1)*BININTERVAL_flt - OVERLAPINTERVAL_flt <= \
                        PointsToCheck_array[Point_int] < \
                        CurrentBin_int*BININTERVAL_flt + OVERLAPINTERVAL_flt:
                CurrentBin_array = CurrentBin_array + [Point_int]
                
            if (CurrentBin_int)*BININTERVAL_flt - OVERLAPINTERVAL_flt <= \
                        PointsToCheck_array[Point_int] < \
                        CurrentBin_int*BININTERVAL_flt + OVERLAPINTERVAL_flt:
                Overlap_array = Overlap_array + [Point_int]
            if PointsToCheck_array[Point_int] >= \
                        CurrentBin_int*BININTERVAL_flt + OVERLAPINTERVAL_flt:
                CurrentBin_int = CurrentBin_int + 1
                if CurrentBin_array != []:
                    Binning_npArray = Binning_npArray + [CurrentBin_array]
                    CurrentBin_array = []
                while (CurrentBin_int - 1)*BININTERVAL_flt - \
                        OVERLAPINTERVAL_flt < PointsToCheck_array[Point_int]:
                    Point_int = Point_int - 1
            Point_int = Point_int + 1
        if CurrentBin_array != []:
            Binning_npArray = Binning_npArray + [CurrentBin_array]
        return [Binning_npArray, Overlap_array]
        
