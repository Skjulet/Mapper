import numpy as np
import Metric as me
import Lens as le
import Bins as bi
import Clust as cl
import Grapher as gr

class Mapper:
	#behovs default pa metric
	def __init__(self,cloud,metric,lens,bins,overlap,clust):

		self.cloud = cloud

		
		self.metric = me.Metric(metric)
		self.lens = le.Lens(lens,self.metric)
		self.clust = cl.Clust(clust,self.metric)

		self.overlap = overlap
		self.bins = bi.Bins(bins,self.overlap)
		
		#self.filteredcloud ar en array[2][n] forsta indexet ar punkten
		#andra indexet ar vardet pa punkten i filtret
		#self.filteredcloud ar sorterad efter i storleksordning efter 			
		#filtrets skalar
		self.filteredcloud = self.lens.filtered(self.cloud)
		
		#self.binnedfilteredcloud ar en array[2][n] forsta indexet ar punkten
		#andra indexet ar index som sager hur punkten ar binnad
		self.binnedfilteredcloud = self.bins.makebins(self.filteredcloud)
		
		#self.clusteredcloud ar en array[2][n] forsta indexet ar punkten
		#andra indexet ar en lista med klustren som punkten tillhor
		self.clusteredcloud = self.clust.makeclustering(self.binnedfilteredcloud)
		


	def mmetric(self,metric):
		self.metric = me.Metric(metric)

	def mlens(self, lens):
		self.lens = le.Lens(lens,self.metric)

	def moverlap(self,overlap):
		self.overlap = overlap

	def mbins(self,bins):
		self.bins = bins

	def mclust(self,clust):
		self.clust = cl.Clust(clust)



	#Denna funktion visar mapper"bilden"
	def visualize(self):
		gr.Grapher(self.clusteredcloud)
