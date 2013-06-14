import numpy as np

class Clust:
	def __init__(self,clust,metric):
		self.clust = clust
		self.metric = metric
	def makeclustering(self,binnedfilteredcould):
		#print("Prints the binnedfilteredcloud:")
		#print(binnedfilteredcould)
		
