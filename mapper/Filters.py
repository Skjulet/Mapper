'''A Class that applies filters.
'''

import numpy as np

from scipy.spatial import distance

import Metric as me
import Filter_Functions as ff


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


        if self.FilterType_str == 'Test':

	        return np.column_stack((range(0, PointCloud_npArray.shape[0]),
                                np.random.sample(PointCloud_npArray.shape[0])))

        #Ariel must fix variable names for this section since I
        #(Gabriel) doesnt know what names are appropriate.
        elif self.FilterType_str == 'Semantic':
	        D = distance.squareform(distance.pdist(PointCloud_npArray,
	                                metric=self.MetricObject_me.get_metric()))
	        values = np.zeros(len(PointCloud_npArray))
	        for n, row in enumerate(D):
	            D[n][row.argmin()]=np.inf
	            Iterations_int = 0
	            while Iterations_int < 6:
		        D[n][row.argmin()]=np.inf
		        Iterations_int += 1
	            values[n] = D[n][row.argmin()]

	        return np.column_stack((range(0, PointCloud_npArray.shape[0]),
	                                values))
        else:
	        pass


