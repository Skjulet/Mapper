'''Module with collections of Mapper filter functions. Every filter
function returns a list with filter values in the same order as 
PointCloud_npArray.  '''


import numpy as np

from scipy.spatial import distance
from scipy import stats

import Metric as me


def gaussian_kde(PointCloud_npArray, Metric_me):
    ''' Filter that returns the estimated density of the
    points coordinates as filter value.
    '''
    
    
    Kernel
    
    _kernel = stats.gaussian_kde(PointCloud_npArray.transpose())
    FilterValues_npArray = Kernel_kernel(PointCloud_npArray.transpose())
    
    return FilterValues_npArray

def PCA(PointCloud_npArray, Metric_me, NTH_EIGENVECTOR_int=1):
    ''' Filter that returns the projection of the 
    point cloud onto the nth principal component
    as filter value.
    '''
    
    
    return None

def nth_neighbor(PointCloud_npArray, Metric_me, neighbor_int):
    ''' Filter that returns the distance to the nth 
    neighbor as filter value.
    '''
    
    
    DistanceMatrix_npArray = distance.squareform(
                distance.pdist(PointCloud_npArray, 
                               metric=Metric_me.getmetric()))
    FilterValues_npArray = np.zeros(len(PointCloud_npArray))
    
    for n_int, Row in enumerate(DistanceMatrix_npArray):
        DistanceMatrix_npArray[n_int][Row.argmin()] = np.inf
        Iterations_int = 0
        while Iterations_int < neighbor_int + 1:
            DistanceMatrix_npArray[n_int][Row.argmin()] = np.inf
            Iterations_int += 1
            FilterValues_npArray[n_int] = \
                DistanceMatrix_npArray[n_int][Row.argmin()]
    
    return FilterValues_npArray
    
def semantic_filter(PointCloud_npArray, MetricObject_me):
    '''A semantic filter.
    '''


    D = distance.squareform(distance.pdist(PointCloud_npArray,
                                    metric=MetricObject_me.get_metric()))
    values = np.zeros(len(PointCloud_npArray))
    for n, row in enumerate(D):
        D[n][row.argmin()]=np.inf
        Iterations_int = 0
        while Iterations_int < 6:
            D[n][row.argmin()]=np.inf
            Iterations_int += 1
        values[n] = D[n][row.argmin()]
        
    return values
    
    
    
    
