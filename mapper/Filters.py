'''A Class that applies filters.
'''

import numpy as np

from scipy.spatial import distance

import Metric as me
from Filter_Functions import FilterFunctions as ff


class Filters:
    def __init__(self, FilterType_str, MetricObject_me, DebugMode_bol = False):
        '''Initiates a Filters class with a given FilterType_str.
        '''


        self.MetricObject_me = MetricObject_me
        self.FilterType_str = FilterType_str

    def apply_filter(self, PointCloud_npArray):
        '''Applies a filter function gives as self.FilterType_str.
        Filter functions are located in Mapper/mapper/Filter_Functions.
        Implementation of Mapper/mapper/Filter_Functions map needed.
        '''
        
        
        FilterValues_npArray = None

        if self.FilterType_str == 'Test':
            FilterValues_npArray = \
            np.random.sample(PointCloud_npArray.shape[0])
	    
        elif self.FilterType_str == 'Semantic':
            FilterValues_npArray = ff.semantic_filter(PointCloud_npArray,
                                                    self.MetricObject_me)
	                                
        else:
	        pass
	    
        return np.column_stack((range(0, PointCloud_npArray.shape[0]), \
                                                        FilterValues_npArray))


