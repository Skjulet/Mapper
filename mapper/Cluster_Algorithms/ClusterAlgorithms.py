'''A Collection of clustering algorithms.
'''

import numpy as np

from scipy.spatial import distance
from scipy.cluster.hierarchy import linkage
from scipy.cluster.hierarchy import fcluster

class ClusterAlgorithms:
    def __init__(self):
        '''A ClusterAlgorithm object is never used, the functions in 
        the object however is used as clustering algorithms.  '''
        
        
        self.MetricObject_me = None
               
    def cluster_algorithm(self, PointCloud_npArray, MetricObject_me,
                        ClusterAlgorithm_str, ClusterArguments_array):
        '''This method implements the given clustering algorithm. This
        function is always called when implementing a clustering 
        algorithm from another object through 
        ClusterAlgorithms().cluster_algorithm(PointCloud_npArray,
                                            MetricObject_me, 
                                            ClusterAlgorithm_str,
                                            ClusterArguments_array).
        '''
        
        
        self.MetricObject_me = MetricObject_me
        
        if ClusterAlgorithm_str == 'CompleteLinkage':
            return self.complete_linkage_clustering(PointCloud_npArray,
                                                    ClusterArguments_array[0])
                                                                                                      
    #Ariel must fix variable names for this section since I
    #(Gabriel) doesnt know what names are appropriate.
    def complete_linkage_clustering(self, data, EPS_flt):
        '''Complete Linkage clustering method. An epsilon (EPS_flt)
        value is needed to execute the algorithm.  '''
        
        
        X = data
    
        Y = distance.pdist(X, metric = self.MetricObject_me.get_metric())
        Y[Y < 0] = 0
    
        Z = linkage(Y, 'complete')
    
        labels = fcluster(Z, t=EPS_flt, criterion = 'distance')
    
        return labels
