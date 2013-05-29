import numpy as np
import Metric.py as me
import Lens.py as le
import Clust.py as cl
import Grapher.py as gr

class Mapper:
	#behövs default på metric
	def __init__(self,cloud,metric,lens,bins,overlap,clust):

		self.cloud = cloud

		
		self.metric = me.Metric(metric)
		self.lens = le.Lens(lens,self.metric)
		self.clust = cl.Clust(clust)

		self.bins = bins
		self.overlap = overlap
		
		
		#filtered cloud är en array[2][n] första indexet är punkten
		#andra indexet är värdet på punkten i filtret
		#self.filteredcloud är sorterad efter i storleksordning efter 			#filtrets skalär
		self.filteredcloud = self.lens.filter(self.cloud)
		
		
		
		


	def mmetric(self,metric):
		self.metric = me.Metric(metric)

	def mlens(self, lens):
		self.lens = le.Lens(lens,self.metric)

	def moverlap(self,overlap):
		self.overlap = overlap

	def mbins(self,bins):
		self.bins = bins

	def mclust(self,clust):
		self.clust = clust


	#Denna funktion visar mapper"bilden"
	def visualize(self):
		



