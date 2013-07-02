
''' The lens class applies the chosen lens to the point cloud data.
'''


import numpy as np

import Metric as me
from Filter_Functions import FilterFunctions as ff


class Lens:
    def __init__(self, LensName_str, LensArguments_array, MetricObject_me,
                BinsObject_bi, Mother_ma=None):
        '''The Lens object is initiated with a set with four arguments.
        '''
        
        
        self.DebugMode_bol = Mother_ma.DebugMode_bol
        self.Mother_ma = Mother_ma
        self.LensName_str = Mother_ma.LensName_str
        self.LensArguments_array = LensArguments_array
        self.MetricObject_me = MetricObject_me
        self.BinsObject_bi = BinsObject_bi
        
        self.PointCloud_npArray = None
        self.FilteredPointCloud_npArray = None
        
        self.Binning_array = None
        
    def filter_point_cloud(self,PointCloud_npArray):
        '''filter_point_cloud  applies filter from 
        Filter_Functions/FiltersFunctions.py, sorts on filter variable
        and places the points into bins.  '''
        
        
        self.PointCloud_npArray = PointCloud_npArray

        if self.DebugMode_bol == True:
            print("In Lens.filter_point_cloud(): The PointCloud_npArray \
                itself:")
            print(self.PointCloud_npArray)

        #self.FilteredPointCloud_npArray is filtered and sorted after 
        #filter size.
        self.filter_and_sort_points()

        if self.DebugMode_bol == True:
            print("In Lens.filter_point_cloud(): PointCloud_npArray \
                    after filter + sorting")
            print(self.FilteredPointCloud_npArray)
        
        #The self.BinsObject_bi.apply_bins function adds creates an
        #array with binning information.
        [self.Binning_array, Overlap_array] = \
            self.BinsObject_bi.apply_bins(self.FilteredPointCloud_npArray)
            
        
        
        return [self.FilteredPointCloud_npArray, 
                self.Binning_array, 
                Overlap_array]

    def filter_and_sort_points(self):
        '''filter_points applies the filter specified as
        LensName_str to each point in the self.PointCloud_npArray and
        sorts self.FilteredPointCloud_npArray after each points filter
        size.  '''
        
        
        #Creates filter value for each point.
        if self.Mother_ma.UnsortedFilterValues_npArray == None or \
                    len(self.Mother_ma.UnsortedFilterValues_npArray) != \
                    len(self.Mother_ma.PointCloud_npArray):
            self.Mother_ma.UnsortedFilterValues_npArray = \
            ff.FilterFunctions().apply_filter(self.PointCloud_npArray,
                                                self.MetricObject_me, 
                                                self.LensName_str, 
                                                self.LensArguments_array)
        self.FilteredPointCloud_npArray = \
            np.column_stack((range(0, self.PointCloud_npArray.shape[0]),  
                            self.Mother_ma.UnsortedFilterValues_npArray))
        
        if self.Mother_ma.FilterAdded_ToGraphbol == True:
            self.Mother_ma.add_mean_properties('Filter Value', 
                                    self.FilteredPointCloud_npArray[:, 1])
        if self.DebugMode_bol == True:
            print("In Lens.filter_and_sort_points(): Cloud after added \
            filters:")
            print(self.FilteredPointCloud_npArray)
        
        #Sorts self.FilteredPointCloud_npArray on filter value.
        TemporaryFiltered_npArray = np.zeros((
                self.FilteredPointCloud_npArray.shape[0], 
                self.FilteredPointCloud_npArray.shape[1]))
        CountVariable_int = 0
        for Index_flt in np.lexsort((self.FilteredPointCloud_npArray[:,0],
                                    self.FilteredPointCloud_npArray[:,1])):
            TemporaryFiltered_npArray[CountVariable_int] = \
            self.FilteredPointCloud_npArray[Index_flt, :]
            CountVariable_int = CountVariable_int + 1
        self.FilteredPointCloud_npArray = TemporaryFiltered_npArray





