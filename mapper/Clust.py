'''A class that clusters the points in each bin, depending on 
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
        self.Metric_me = MetricObject_me
        self.BFPointCloud_npArray = None
        self.size = len(PointCloud_npArray)
        
    def create_clustering(self, BFPointCloud_npArray):
        '''Creates clustering from each bin given in the binning data 
        of BFPointCloud_npArray.  '''
        
        
        self.BFPointCloud_npArray = BFPointCloud_npArray
        if self.DebugMode_bol == True:
            print("In clust.TESTmakeclustering:Data to be clustered:")
            print(self.BFPointCloud_npArray)
    
        firstbin = [self.BFPointCloud_npArray[0,0]]

        secondbin = []
        for index in range(1,len(self.BFPointCloud_npArray)):

            if self.BFPointCloud_npArray[index,2] == 2:
                firstbin = firstbin + [self.BFPointCloud_npArray[index,0]]
                secondbin = secondbin + [self.BFPointCloud_npArray[index,0]]
            elif self.BFPointCloud_npArray[index,2] == 1 \
                            and self.BFPointCloud_npArray[index-1,2] == 2:
                self.createclusters(firstbin,index)
                firstbin = secondbin
                firstbin = firstbin + [self.BFPointCloud_npArray[index,0]]
                secondbin = []	
            elif self.BFPointCloud_npArray[index,2] == 1 \
                            and self.BFPointCloud_npArray[index-1,2] == 1:
                firstbin = firstbin + [self.BFPointCloud_npArray[index,0]]

        index = index +1
        self.createclusters(firstbin,index)

        return self.BFPointCloud_npArray

    def createclusters(self, points, loopnumber):
        '''
        '''
        
        
        if self.DebugMode_bol == True:
            print("In clust.createclusters:")
            print(points)

        #gives each cluster unique index
        if self.BFPointCloud_npArray.shape[1] == 3:
            maxclust = 0
        else:
            maxclust = max(self.BFPointCloud_npArray[:,-1])
    
        a = np.append(np.ones(loopnumber-len(points))*(-2),
                      [x+maxclust for x in 
                       self.clusteringmethod(
                        self.PointCloud_npArray[points,:])])
    
        self.BFPointCloud_npArray = np.column_stack(
                            (self.BFPointCloud_npArray,
                             np.append(a,np.ones(self.size-loopnumber)*(-2))))

    def clusteringmethod(self, PointCloud_npArray):
        '''
        '''
        
        
        if self.ClusterAlgorithm_str == 'CompleteLinkage':
            return self.SLcluster( PointCloud_npArray, self.EPS_flt)
    
    
    def SLcluster(self, data, EPS_flt):
        '''
        '''
        
        
        X = data
    
        Y = distance.pdist(X, metric=self.Metric_me.get_metric())
        Y = Y / np.max(Y)
        Y[Y<0] = 0
    
        Z = linkage(Y,'complete')
    
        labels = fcluster(Z,t=EPS_flt,criterion='distance')
    
        return labels
