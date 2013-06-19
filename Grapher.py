import numpy as np
import networkx as nx

class Grapher:
	def __init__(self,cloud,clusteredcloud,debugmode = False):
		self.debugmode = debugmode

		self.cloud = cloud
		self.clusteredcloud = clusteredcloud
		self.TheGraph = nx.Graph()
		self.GraphIndexArray = []
		self.EdgeIndexArray = []

	def GetGraph(self):
		return self.TheGraph

	def makegraph(self):

		if self.debugmode == True:
			print("In Grapher.TESTmakegraph:Data to be graphed:")
			print(self.clusteredcloud[:,[0,1,2,3]])

		cntvar = 0
		columnindex = 3
		while cntvar < len(self.cloud):
			if cntvar > 0 and self.clusteredcloud[cntvar,columnindex] == -2 :
				
				while self.clusteredcloud[cntvar-1,2] == 2:
					cntvar = cntvar-1
				columnindex = columnindex +1
			if columnindex > 3 and self.clusteredcloud[cntvar,columnindex-1] != -2:
				self.EdgeIndexArray = self.EdgeIndexArray + [[self.clusteredcloud[cntvar,columnindex],self.clusteredcloud[cntvar,columnindex-1],cntvar]]
			self.GraphIndexArray = self.GraphIndexArray + [[self.clusteredcloud[cntvar,columnindex],cntvar]]
			cntvar = cntvar+1

		self.insertgraphs()
	

	def insertgraphs(self):
		if self.debugmode == True:
			#print("In Graph.insertgraph:")
			#print(points)
			pass
		clusters = set()
		usededges = set()
		
		for aPoint in self.GraphIndexArray:

			#print(aPoint)
			
			if aPoint[0] not in clusters:
				self.TheGraph.add_node(aPoint[0],NumberOfPoints = 1)
			else:
				self.TheGraph.node[aPoint[0]]['NumberOfPoints'] += 1
			clusters.add(aPoint[0])
			
		
		for AnEdge in self.EdgeIndexArray:
			if (AnEdge[0],AnEdge[1]) not in usededges:
				self.TheGraph.add_edge(AnEdge[0],AnEdge[1])
			usededges.add((AnEdge[0],AnEdge[1]))
		

	def addlabels(self,labels):

		clusters = set()
		usededges = set()
		
		for aPoint in self.GraphIndexArray:
			if aPoint[0] not in clusters:
				self.TheGraph.node[aPoint[0]]['Label'] = str(labels[self.clusteredcloud[aPoint[1],0]])
			else:
				self.TheGraph.node[aPoint[0]]['Label'] += ', ' + str(labels[self.clusteredcloud[aPoint[1],0]])
			clusters.add(aPoint[0])






	
