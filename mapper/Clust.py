'''A class that clusters the PointBin_array in each bin, depending on 
clustering algorithm and the EPS_flt parameter.  '''


import numpy as np

from scipy.spatial import distance
from scipy.cluster.hierarchy import linkage
from scipy.cluster.hierarchy import fcluster


class Clust:
    def __init__(self, PointCloud_npArray, ClusterAlgorithm_str, EPS_flt,
                 MetricObject_me, DebugMode_bol=False):
        '''Initiates the object with a PointCloud_npArray, a clustering
        algorithm and an EPS_flt value. The clustering is different 
        depending on the given metric in the MetricObject_me.  '''
        
        
        self.DebugMode_bol = DebugMode_bol
        
        self.PointCloud_npArray = PointCloud_npArray
        self.ClusterAlgorithm_str = ClusterAlgorithm_str
        self.EPS_flt = EPS_flt
        self.MetricObject_me = MetricObject_me
        self.BFPointCloud_npArray = None
        self.PointCloudSize_int = len(PointCloud_npArray)
        
    def create_clustering(self, BFPointCloud_npArray):
        '''Creates clustering from each bin given in the binning data 
        of BFPointCloud_npArray.  '''
        
        
        self.BFPointCloud_npArray = BFPointCloud_npArray
        if self.DebugMode_bol == True:
            print("In clust.TESTmakeclustering:Data to be clustered:")
            print(self.BFPointCloud_npArray)
    
        FirstBin_array = [self.BFPointCloud_npArray[0, 0]]
        SecondBin_array = []
        for PointNr_int in range(1, self.PointCloudSize_int):

            if self.BFPointCloud_npArray[PointNr_int, 2] == 2:
                FirstBin_array = FirstBin_array + \
                [self.BFPointCloud_npArray[PointNr_int, 0]]
                SecondBin_array = SecondBin_array + \
                [self.BFPointCloud_npArray[PointNr_int, 0]]
                
            elif self.BFPointCloud_npArray[PointNr_int, 2] == 1 \
                        and self.BFPointCloud_npArray[PointNr_int-1, 2] == 2:
                self.cluster_bin(FirstBin_array,PointNr_int)
                FirstBin_array = SecondBin_array
                FirstBin_array = FirstBin_array + \
                [self.BFPointCloud_npArray[PointNr_int,0]]
                SecondBin_array = []
                
            elif self.BFPointCloud_npArray[PointNr_int, 2] == 1 \
                        and self.BFPointCloud_npArray[PointNr_int-1, 2] == 1:
                FirstBin_array = FirstBin_array + \
                [self.BFPointCloud_npArray[PointNr_int, 0]]

        PointNr_int = PointNr_int + 1    #compensates for last point
        self.cluster_bin(FirstBin_array, PointNr_int)

        return self.BFPointCloud_npArray

    def cluster_bin(self, PointBin_array, PointNr_int):
        '''Clusters a bin with a clustering algorithm specified in 
        cluster_algorithm.  '''
        
        
        if self.DebugMode_bol == True:
            print("In clust.createclusters:")
            print(PointBin_array)

        #Gives each cluster a unique index.
        if self.BFPointCloud_npArray.shape[1] == 3:
            MaxClustNr_int = 0
        else:
            MaxClustNr_int = max(self.BFPointCloud_npArray[:,-1])
    
        TempClust_array = np.append(np.ones(
                        PointNr_int - len(PointBin_array))*(-2),
                        [x + MaxClustNr_int for x in 
                        self.cluster_algorithm(
                        self.PointCloud_npArray[PointBin_array, :])])
    
        self.BFPointCloud_npArray = np.column_stack(
                        (self.BFPointCloud_npArray,
                        np.append(TempClust_array, 
                        np.ones(self.PointCloudSize_int - PointNr_int)*(-2))))

    def cluster_algorithm(self, PointCloud_npArray):
        '''This method implements the given clustering algorithm.
        '''
        
        
        if self.ClusterAlgorithm_str == 'CompleteLinkage':
            return self.complete_linkage_clustering(PointCloud_npArray,
                                                    self.EPS_flt)
    
    
    
    #Ariel must fix variable names for this section since I
    #(Gabriel) doesnt know what names are appropriate.
    def complete_linkage_clustering(self, data, EPS_flt):
        '''Complete Linkage clustering method.
        '''
        
        
        X = data
    
        Y = distance.pdist(X, metric = self.MetricObject_me.get_metric())
        Y = Y / np.max(Y)
        Y[Y < 0] = 0
    
        Z = linkage(Y, 'complete')
    
        labels = fcluster(Z, t=EPS_flt, criterion = 'distance')
    
        return labels
