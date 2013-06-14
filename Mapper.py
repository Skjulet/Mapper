import numpy as np
import Metric as me
import Lens as le
import Bins as bi
import Clust as cl
import Grapher as gr

class Mapper:
	#default values may be needed
	def __init__(self,cloud,metric,lens,bins,overlap,clust,debugmode = False):
		

		self.cloud = cloud

		self.metric = me.Metric(metric)
		
		self.overlap = overlap

		self.bins = bi.Bins(bins, self.overlap, equalize = True)
		

		self.lens = le.Lens(lens,self.metric,self.bins)
		self.clust = cl.Clust(clust,self.metric)
		
		self.debugmode = debugmode
		if self.debugmode == True:
			print("Mapper is now running in debug mode")	
			print()	

		#fix comment
		'''
		self.filteredcloud is an array[3][n] the first index is the index of
		the first point in self.cloud ie if we consider 
		self.filteredcloud[1,b], then self.filteredcloud[1,b] corresponds to
		the point self.cloud(:,self.filteredcloud[1,b])
		the second index is the value the filter assigns to the point
		the third index describes binning
		self.filteredcloud is sorted after the size of the filters scalar
		the filteredcloud is also binned
		'''		
		self.filteredcloud = self.lens.filtered(self.cloud)
		if self.debugmode == True:
			print("Printing self.filteredcloud in the Mapper object:")
			print(self.filteredcloud)	

		#fix comment
		'''
		self.clusteredcloud is an array[2][n] the first index is a point
		the second index is a list with the clusters the point is in
		'''
	#this may be changed/rethought
		self.clusteredcloud = self.clust.makeclustering(self.filteredcloud)


		if self.debugmode == True:
			print("Printing self.clusteredcloud in the Mapper object:")
			print(self.clusteredcloud)	
		


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



	#This function shows the mapper visualization
	def visualize(self):
		gr.Grapher(self.clusteredcloud)