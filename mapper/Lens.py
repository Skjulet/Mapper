
''' The lens class applies the chosen lens to the point cloud data.
'''


import numpy as np

import Metric as me
from Filter_Functions import FilterFunctions as ff


class Lens:
    def __init__(self, LensName_str, LensArguments_array, MetricObject_me,
                BinsObject_bi, DebugMode_bol=False, Mother_ma=None):
        '''The Lens object is initiated with a set with four arguments.
        '''
        
        
        self.DebugMode_bol = DebugMode_bol
        
        self.LensName_str = Mother_ma.LensName_str
        self.LensArguments_array = LensArguments_array
        self.MetricObject_me = MetricObject_me
        self.BinsObject_bi = BinsObject_bi
        
        self.PointCloud_npArray = None
        
        #self.BFPointCloud_npArray works towards becoming a binned and
        #filtered point cloud throughout the algorithm.
        self.BFPointCloud_npArray = None
  
    def filter_point_cloud(self,PointCloud_npArray):
        '''filter_point_cloud  applies filter from 
        Filter_Functions/FiltersFunctions.py, sorts on filter variable
        and places the points into bins.  '''
        
        
        self.PointCloud_npArray = PointCloud_npArray

        if self.DebugMode_bol == True:
            print("In Lens.filter_point_cloud(): The PointCloud_npArray \
                itself:")
            print(self.PointCloud_npArray)

        #self.BFPointCloud_npArray is filtered and sorted after filter
        #size.
        self.filter_and_sort_points()

        if self.DebugMode_bol == True:
            print("In Lens.filter_point_cloud(): PointCloud_npArray \
                    after filter + sorting")
            print(self.BFPointCloud_npArray)

        #The self.BinsObject_bi.applybins function adds binning data to
        #the self.BFPointCloud_npArray as a new column.
        self.BFPointCloud_npArray = \
            self.BinsObject_bi.apply_bins(self.BFPointCloud_npArray)
        
        return self.BFPointCloud_npArray

    def filter_and_sort_points(self):
        '''filter_points applies the filter specified as
        LensName_str to each point in the self.PointCloud_npArray and
        sorts self.BFPointCloud_npArray after each points filter size.
        '''
        
        
        #Creates filter value for each point.
        self.BFPointCloud_npArray = \
            ff.FilterFunctions().apply_filter(self.PointCloud_npArray,
            self.MetricObject_me, self.LensName_str, self.LensArguments_array)
        if self.DebugMode_bol == True:
            print("In Lens.filter_and_sort_points(): Cloud after added \
            filters:")
            print(self.BFPointCloud_npArray)
        
        #Sorts self.BFPointCloud_npArray on filter value.
        TemporaryFiltered_npArray = np.zeros((
                self.BFPointCloud_npArray.shape[0], 
                self.BFPointCloud_npArray.shape[1]))
        CountVariable_int = 0
        for Index_flt in np.lexsort((self.BFPointCloud_npArray[:,0],
                                    self.BFPointCloud_npArray[:,1])):
            TemporaryFiltered_npArray[CountVariable_int] = \
            self.BFPointCloud_npArray[Index_flt, :]
            CountVariable_int = CountVariable_int + 1
        self.BFPointCloud_npArray = TemporaryFiltered_npArray





