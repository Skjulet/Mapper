'''A class that clusters the PointBin_array in each bin, depending on 
clustering algorithm and the ClusterArguments_array parameter.  '''


import numpy as np

from scipy.spatial import distance
from scipy.cluster.hierarchy import linkage
from scipy.cluster.hierarchy import fcluster

from Cluster_Algorithms import ClusterAlgorithms as ca


class Clust:
    def __init__(self, PointCloud_npArray, ClusterAlgorithm_str, 
                ClusterArguments_array, MetricObject_me, Mother_ma=None):
        '''Initiates the object with a PointCloud_npArray, a clustering
        algorithm and an ClusterArguments_array value. The clustering is different 
        depending on the given metric in the MetricObject_me.  '''
        
        
        self.DebugMode_bol = Mother_ma.DebugMode_bol
        
        self.PointCloud_npArray = PointCloud_npArray
        self.ClusterAlgorithm_str = ClusterAlgorithm_str
        self.ClusterArguments_array = ClusterArguments_array
        self.MetricObject_me = MetricObject_me
        self.BFPointCloud_npArray = None
        self.PointCloudSize_int = len(PointCloud_npArray)
        

    def create_clustering(self, FilteredPointCloud_npArray, 
                        Binning_array):
        '''Creates clustering from each bin given in the binning data 
        of Binning_array.  '''
        
        
        
        self.FilteredPointCloud_npArray = FilteredPointCloud_npArray
        self.Binning_array = Binning_array
        self.Clustering_array = []
        MaxClust_int = 0
        if self.DebugMode_bol == True:
            print("In clust.create_clustering():Data to be clustered:")
            print(self.FilteredPointCloud_npArray)
        TemporaryClustering_array = None
        for aBin_array in self.Binning_array:
            TemporaryClustering_array = self.cluster_algorithm(
                    self.PointCloud_npArray[
                    self.FilteredPointCloud_npArray[aBin_array, 0].tolist(),
                    :])
            for BinIndex_int in range(0,len(aBin_array)):
                self.Clustering_array = self.Clustering_array + \
                [[TemporaryClustering_array[BinIndex_int] + MaxClust_int,\
                aBin_array[BinIndex_int]]]
            MaxClust_int = MaxClust_int + max(TemporaryClustering_array)
        return self.Clustering_array

    def cluster_algorithm(self, PointCloud_npArray):
        '''This method implements the given clustering algorithm.
        '''
        
        
        return ca.ClusterAlgorithms().cluster_algorithm(PointCloud_npArray,
        self.MetricObject_me, self.ClusterAlgorithm_str,
        self.ClusterArguments_array)
    

