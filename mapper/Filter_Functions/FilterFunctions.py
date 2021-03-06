'''Module with collections of Mapper filter functions. Every filter
function returns a list with filter values in the same order as 
PointCloud_npArray.  '''


import numpy as np

from scipy.spatial import distance
from scipy import stats

import Metric as me


class FilterFunctions:
    def __init__(self):
        '''A FilterFunctions object is never used, the functions in 
        the object however is used as filter functions.  '''
        
        
        self.MetricObject_me = None
        
    def apply_filter(self, PointCloud_npArray, MetricObject_me,
                        FilterType_str, FilterArguments_array):
        '''This method implements the given filter function. This
        function is always called when implementing a filter from
        another object through 
        FilterFunctions().apply_filter(PointCloud_npArray, 
                                        MetricObject_me,
                                        LensName_str,
                                        LensArguments_array).  '''
        
        self.MetricObject_me = MetricObject_me
        
        FilterValues_npArray = None

        if FilterType_str == 'Test':
            FilterValues_npArray = \
            np.random.sample(PointCloud_npArray.shape[0])
        
        elif FilterType_str == 'nth_neighbor':
            if len(FilterArguments_array) == 0:
                FilterValues_npArray = self.nth_neighbor(PointCloud_npArray)
            else:
                FilterValues_npArray = self.nth_neighbor(PointCloud_npArray, 
                                                    FilterArguments_array[0])
        
        elif FilterType_str == 'Gaussian_KDE':
            FilterValues_npArray = self.gaussian_kde(PointCloud_npArray)
            
        elif FilterType_str == 'PCA':
            if len(FilterArguments_array) == 0:
                FilterValues_npArray = self.PCA(PointCloud_npArray)
            else:
                FilterValues_npArray = self.PCA(PointCloud_npArray, 
                                                    FilterArguments_array[0])
        
        elif FilterType_str == 'word_distance':
            FilterValues_npArray = self.word_distance(PointCloud_npArray,
                                                    FilterArguments_array[0])
        
        else:
            pass
        
        return FilterValues_npArray


    def gaussian_kde(self, PointCloud_npArray):
        ''' Filter that returns the estimated density of the
        point cloud coordinates as filter value.
        '''
        
        
        Kernel_kernel = stats.gaussian_kde(PointCloud_npArray.transpose())
        FilterValues_npArray = Kernel_kernel(PointCloud_npArray.transpose())
        
        return FilterValues_npArray

    def PCA(self, PointCloud_npArray, NTH_EIGENVECTOR_int=1):
        ''' Filter that returns the projection of the 
        point cloud onto the nth principal component
        as filter value.
        '''
        
        
        return None

    def nth_neighbor(self, PointCloud_npArray, neighbor_int=5):
        ''' Filter that returns the distance to the nth 
        neighbor as filter value.
        '''
        
        
        DistanceMatrix_npArray = distance.squareform(
                distance.pdist(np.array(PointCloud_npArray, dtype=np.int32),
                               metric=self.MetricObject_me.get_metric()))
        FilterValues_npArray = np.zeros(len(PointCloud_npArray))
        
        for n_int, Row in enumerate(DistanceMatrix_npArray):
            DistanceMatrix_npArray[n_int][Row.argmin()] = np.inf
            Iterations_int = 0
            while Iterations_int < neighbor_int + 1:
                DistanceMatrix_npArray[n_int][Row.argmin()] = np.inf
                Iterations_int = Iterations_int + 1
            FilterValues_npArray[n_int] = \
                DistanceMatrix_npArray[n_int][Row.argmin()]
        
        return FilterValues_npArray
        
    def word_distance(self, PointCloud_npArray, WordVector_npArray):
        '''A function that measures the distance between a given word (given 
        as a vector np.array) and every other word and saves the distance as 
        an np.array.  '''
        
        FilterValues_npArray = np.zeros(len(PointCloud_npArray))
        FilterValues_npArray = \
        distance.cdist(np.array(PointCloud_npArray, dtype=np.int32),
                        WordVector_npArray,
                        metric=self.MetricObject_me.get_metric())
                
        
        return FilterValues_npArray
        
        
        
