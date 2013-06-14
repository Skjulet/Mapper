import numpy as np

class Clust:
	def __init__(self,clust,metric):
		self.clust = clust
		self.metric = metric
	def makeclustering(self,binnedfilteredcould):
		print("Data to be clustered:")
		print(binnedfilteredcould)

		firstbin = [(binnedfilteredcould[0,0],0)]
		print(firstbin)
		secondbin = []
		for index in range(1,len(binnedfilteredcould)):
			print(binnedfilteredcould[index,2])
			
			if binnedfilteredcould[index,2] == 2:
				firstbin = firstbin + [(binnedfilteredcould[index,0],0)]
				secondbin = secondbin + [(binnedfilteredcould[index,0],0)]
			elif binnedfilteredcould[index,2] == 3:
				
			
		
	def createclusters(self,points):
		pass
