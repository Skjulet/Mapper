import numpy as np
from scipy.spatial import distance
from scipy.cluster.hierarchy import linkage
from scipy.cluster.hierarchy import fcluster

class Clust:
	def __init__(self,cloud,clust,eps,metric,debugmode = False):
		self.debugmode = debugmode
		
		self.cloud = cloud
		self.clust = clust
		self.eps = eps
		self.metric = metric
		self.binnedfilteredcould = None
		self.size = len(cloud)
	def TESTmakeclustering(self,binnedfilteredcould):
		self.binnedfilteredcould = binnedfilteredcould
		if self.debugmode == True:
			print("In clust.TESTmakeclustering:Data to be clustered:")
			print(self.binnedfilteredcould)

		firstbin = [self.binnedfilteredcould[0,0]]
		
		secondbin = []
		for index in range(1,len(self.binnedfilteredcould)):
			
			if self.binnedfilteredcould[index,2] == 2:
				firstbin = firstbin + [self.binnedfilteredcould[index,0]]
				secondbin = secondbin + [self.binnedfilteredcould[index,0]]
			elif self.binnedfilteredcould[index,2] == 1 and self.binnedfilteredcould[index-1,2] == 2:
				self.createclusters(firstbin,index)
				firstbin = secondbin
				firstbin = firstbin + [self.binnedfilteredcould[index,0]]
				secondbin = []	
			elif self.binnedfilteredcould[index,2] == 1 and self.binnedfilteredcould[index-1,2] == 1:
				firstbin = firstbin + [self.binnedfilteredcould[index,0]]
		
		index = index +1
		self.createclusters(firstbin,index)
		
		return self.binnedfilteredcould

	def createclusters(self,points,loopnumber):
		if self.debugmode == True:
			print("In clust.createclusters:")
			print(points)
		
		#gives each cluster unique index
		if self.binnedfilteredcould.shape[1] == 3:
			maxclust = 0
		else:
			maxclust = max(self.binnedfilteredcould[:,-1])

		a = np.append(np.ones(loopnumber-len(points))*(-2),[x+maxclust for x in self.clusteringmethod(self.cloud[points,:])])

		self.binnedfilteredcould = np.column_stack((self.binnedfilteredcould, np.append(a,np.ones(self.size-loopnumber)*(-2))))
		

	def clusteringmethod(self,cloud):
		if self.clust == 'CompleteLinkage':
			return self.SLcluster( cloud, self.eps)


	def SLcluster(self,data, eps):
		X = data

		Y = distance.pdist(X, metric=self.metric.getmetric())
		Y = Y / np.max(Y)
		Y[Y<0] = 0

		Z = linkage(Y,'complete')

		labels = fcluster(Z,t=eps,criterion='distance')

		return labels

