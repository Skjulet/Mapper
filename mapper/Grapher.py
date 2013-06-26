'''This class creates a graph from the binned and clustered point cloud
data using networkx.
'''

import numpy as np

import networkx as nx


class Grapher:
    def __init__(self, PointCloud_npArray, ClusteredPointCloud_npArray,
                DebugMode_bol = False):
        '''PointCloud_npArray and ClusteredPointCloud_npArray are used
        to generate the graph with self.create_graph().  '''


        self.debugmode = DebugMode_bol
        
        self.PointCloud_npArray = PointCloud_npArray
        self.ClusteredPointCloud_npArray = ClusteredPointCloud_npArray
        self.TheGraph_graph = nx.Graph()
        self.GraphIndex_array = []
        self.EdgeIndex_array = []
        
        self.create_graph()

    def get_graph(self):
        '''Returns the graph.
        '''
        
        
        return self.TheGraph_graph

    def create_graph(self):
        '''create_graph creates the graph when object is initiated.
        '''
        
        
        if self.debugmode == True:
            print("In Grapher.TESTmakegraph:Data to be graphed:")
            print(self.ClusteredPointCloud_npArray[:, [0, 1, 2, 3]])

        RowCnt_int = 0
        ColumnCnt_int = 3
        while RowCnt_int < len(self.PointCloud_npArray):
            if RowCnt_int > 0 and \
            self.ClusteredPointCloud_npArray[RowCnt_int, ColumnCnt_int] == -2:
                while self.ClusteredPointCloud_npArray[RowCnt_int - 1, 2] == 2:
	                RowCnt_int = RowCnt_int - 1
                ColumnCnt_int = ColumnCnt_int + 1
            if ColumnCnt_int > 3 and \
            self.ClusteredPointCloud_npArray[RowCnt_int, 
            ColumnCnt_int-1] != -2:
                self.EdgeIndex_array = self.EdgeIndex_array + \
                [[self.ClusteredPointCloud_npArray[RowCnt_int, ColumnCnt_int],
                self.ClusteredPointCloud_npArray[RowCnt_int, ColumnCnt_int-1],
                RowCnt_int]]
            self.GraphIndex_array = self.GraphIndex_array + \
            [[self.ClusteredPointCloud_npArray[RowCnt_int, ColumnCnt_int],
            RowCnt_int]]
            RowCnt_int = RowCnt_int + 1

        self.initiate_graph()

    def initiate_graph(self):
        '''Inserts the nodes and edges from self.GraphIndex_array and 
        self.EdgeIndex_array and inserts them into self.TheGraph_graph.
        '''
        
        
        if self.debugmode == True:
            #print("In Graph.insertgraph:")
            #print(points)
            pass
            
        UsedClusters_set = set()
        for aPoint in self.GraphIndex_array:

            if aPoint[0] not in UsedClusters_set:
                self.TheGraph_graph.add_node(aPoint[0], NumberOfPoints = 1)
            else:
                self.TheGraph_graph.node[aPoint[0]]['NumberOfPoints'] = 1 + \
                self.TheGraph_graph.node[aPoint[0]]['NumberOfPoints']
            UsedClusters_set.add(aPoint[0])

        UsedEdges_set = set()
        for AnEdge in self.EdgeIndex_array:
            if (AnEdge[0], AnEdge[1]) not in UsedEdges_set:
                self.TheGraph_graph.add_edge(AnEdge[0], AnEdge[1])
            UsedEdges_set.add((AnEdge[0], AnEdge[1]))

    def add_labels(self, labels):
        '''Adds labeling data to the nodes in self.TheGraph_graph.
        '''
        
        
        UsedClusters_set = set()
        for aPoint in self.GraphIndex_array:
            if aPoint[0] not in UsedClusters_set:
                self.TheGraph_graph.node[aPoint[0]]['Label'] = \
                str(labels[self.ClusteredPointCloud_npArray[aPoint[1], 0]])
            else:
                self.TheGraph_graph.node[aPoint[0]]['Label'] = \
                self.TheGraph_graph.node[aPoint[0]]['Label'] + ', ' + \
                str(labels[self.ClusteredPointCloud_npArray[aPoint[1], 0]])
            UsedClusters_set.add(aPoint[0])


