import numpy as np
import networkx as nx

class Grapher:
	def __init__(self,cloud,clusteredcloud,labels,properties,debugmode = False):
		self.debugmode = debugmode

		self.cloud = cloud
		self.clusteredcloud = clusteredcloud
		self.labels = labels
		self.properties = properties
		self.TheGraph = nx.Graph()

	def TESTmakegraph(self):

		if self.debugmode == True:
			print("In Grapher.makegraph:Data to be graphed:")
			print(self.clusteredcloud[:,[0,1,2,3]])

		thebin = []
		edges = []
		cntvar = 0
		columnindex = 3
		while cntvar < len(self.cloud):
			
			if cntvar > 0 and self.clusteredcloud[cntvar,columnindex] == -2 :
				self.insertgraphs(thebin,edges,columnindex)
				while self.clusteredcloud[cntvar-1,2] == 2:
					cntvar = cntvar-1
				thebin = []
				edges = []
				columnindex = columnindex +1
			if columnindex > 3 and self.clusteredcloud[cntvar,columnindex-1] != -2:
				edges = edges + [cntvar]
			thebin = thebin + [cntvar]
			cntvar = cntvar+1

		self.insertgraphs(thebin,edges,columnindex)

		return self.TheGraph


	def makegraph(self):

		if self.debugmode == True:
			print("In Grapher.makegraph:Data to be graphed:")
			print(self.clusteredcloud[:,[0,1,2,3]])

		thebin = []
		edges = []
		cntvar = 0
		columnindex = 3
		while cntvar < len(self.cloud):
			
			if cntvar > 0 and self.clusteredcloud[cntvar,columnindex] == -2 :
				self.insertgraphs(thebin,edges,columnindex)
				while self.clusteredcloud[cntvar-1,2] == 2:
					cntvar = cntvar-1
				thebin = []
				edges = []
				columnindex = columnindex +1
			if columnindex > 3 and self.clusteredcloud[cntvar,columnindex-1] != -2:
				edges = edges + [cntvar]
			thebin = thebin + [cntvar]
			cntvar = cntvar+1

		self.insertgraphs(thebin,edges,columnindex)

		return self.TheGraph

	def insertgraphs(self,points,edges,columnindex):
		if self.debugmode == True:
			#print("In Graph.insertgraph:")
			#print(points)
			pass
		clusters = set()
		usededges = set()
		for apoint in points:
			if self.clusteredcloud[apoint,columnindex] not in clusters:
				self.TheGraph.add_node(self.clusteredcloud[apoint,columnindex],NumberOfPoints = 1,Filtervalue =  np.float(self.clusteredcloud[apoint,1]), label = str(self.labels[self.clusteredcloud[apoint,0]]))
			else:
				self.TheGraph.node[self.clusteredcloud[apoint,columnindex]]['label'] += ', ' +str(self.labels[self.clusteredcloud[apoint,0]])
				self.TheGraph.node[self.clusteredcloud[apoint,columnindex]]['Filtervalue'] = (self.TheGraph.node[self.clusteredcloud[apoint,columnindex]]['Filtervalue']*self.TheGraph.node[self.clusteredcloud[apoint,columnindex]]['NumberOfPoints'] + np.float(self.clusteredcloud[apoint,1]))/(self.TheGraph.node[self.clusteredcloud[apoint,columnindex]]['NumberOfPoints']+1)
				self.TheGraph.node[self.clusteredcloud[apoint,columnindex]]['NumberOfPoints'] += 1
			clusters.add(self.clusteredcloud[apoint,columnindex])

		for anedge in edges:
			if (self.clusteredcloud[anedge,columnindex],self.clusteredcloud[anedge,columnindex-1]) not in usededges:
				self.TheGraph.add_edge(self.clusteredcloud[anedge,columnindex],self.clusteredcloud[anedge,columnindex-1])
			usededges.add((self.clusteredcloud[anedge,columnindex],self.clusteredcloud[anedge,columnindex-1]))	






	
