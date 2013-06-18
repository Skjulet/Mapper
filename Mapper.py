import numpy as np
import Metric as me
import Lens as le
import Bins as bi
import Clust as cl
import Grapher as gr
import networkx as nx

class Mapper:
	#default values may be needed
	def __init__(self,cloud,metric,lens,bins,overlap,clust,eps,debugmode = False):
		
		self.debugmode = debugmode
		if self.debugmode == True:
			print("In Mapper__init__: Mapper is now running in debug mode")	
			print()	

		
		self.cloud = cloud

		self.metric = me.Metric(metric,self.debugmode)
		
		self.overlap = overlap

		self.bins = bi.Bins(bins, self.overlap, equalize = True, debugmode = self.debugmode)
		
		self.lens = le.Lens(lens,self.metric,self.bins,debugmode = False)

		self.eps = eps

		self.clust = cl.Clust(self.cloud,clust,self.eps,self.metric,self.debugmode)
		
		self.coloring = None
		
		self.grapherobject = None

		self.properties = None
	
		self.labels = None

		#fix comment
		self.filteredcloud = self.lens.filtered(self.cloud)
		if self.debugmode == True:
			print("In Mapper__init__: Printing self.filteredcloud in the Mapper object:")
			print(self.filteredcloud)	

		#fix comment
		self.clusteredcloud = self.clust.TESTmakeclustering(self.filteredcloud)


		if self.debugmode == True:
			print("In Mapper__init__: Printing self.clusteredcloud:")
			print(self.clusteredcloud)
		


	def mmetric(self,metric):
		self.metric = me.Metric(metric,self.debugmode)

	def mlens(self, lens):
		self.lens = le.Lens(lens,self.metric,self.bins,self.debugmode)

	def moverlap(self,overlap):
		self.overlap = overlap

	def mbins(self,bins):
		self.bins = bins

	def mclust(self,clust):
		self.clust = cl.Clust(cloud,clust,self.metric,self.debugmode)

	def addlabels(self,labels):
		self.labels = labels

	def addproperties(self,properties):
		self.properties = np.column_stack((self.properties, properties))

	#This function shows the mapper visualization
	def visualize(self):
		self.grapherobject = gr.Grapher(self.cloud,self.clusteredcloud,self.labels,self.properties,True)

		#self.grapherobject.makegraph()
		#self.grapherobject.makegraph()
		nx.write_graphml(self.grapherobject.makegraph(), 'graph_files/' + 'TestGraph' + '.graphml')















