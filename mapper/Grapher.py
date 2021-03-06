'''This class creates a graph from the binned and clustered point cloud
data using networkx.
'''


import numpy as np

import networkx as nx


class Grapher:
    def __init__(self, PointCloud_npArray, FilteredPointCloud_npArray,
                Clustering_array, Overlap_array,
                Mother_ma=None):
        '''PointCloud_npArray and FilteredPointCloud_npArray are used
        to generate the graph with self.create_graph().  '''


        self.DebugMode_bol = Mother_ma.DebugMode_bol
        
        self.PointCloud_npArray = PointCloud_npArray
        self.FilteredPointCloud_npArray = FilteredPointCloud_npArray
        self.TheGraph_graph = nx.Graph()
        
        self.NodeIndex_array = Clustering_array
        self.Overlap_array = Overlap_array
        self.EdgeIndex_array = []
        
        self.create_graph()

    def get_graph(self):
        '''Returns the graph.
        '''
        
        
        return self.TheGraph_graph

    def create_graph(self):
        '''Inserts the nodes and edges from self.NodeIndex_array and 
        self.EdgeIndex_array and inserts them into self.TheGraph_graph.
        '''
        
            
        UsedClusters_set = set()
        UnfinishedEdges_array = []
        for aNode_array in self.NodeIndex_array:
            if UnfinishedEdges_array != []:
                
                if aNode_array[1] == UnfinishedEdges_array[0][1]:
                    self.EdgeIndex_array = self.EdgeIndex_array + \
                    [[aNode_array[0]] + UnfinishedEdges_array[0]]
                    UnfinishedEdges_array.pop(0)
            if aNode_array[1] == self.Overlap_array[0]:
                self.Overlap_array.pop(0)
                UnfinishedEdges_array = UnfinishedEdges_array + \
                [[aNode_array[0], aNode_array[1]]]
            if aNode_array[0] not in UsedClusters_set:
                self.TheGraph_graph.add_node(aNode_array[0],
                                            NumberOfPoints = 1)
            else:
                self.TheGraph_graph.node[aNode_array[0]]['NumberOfPoints'] = \
                1 + self.TheGraph_graph.node[aNode_array[0]]['NumberOfPoints']
            UsedClusters_set.add(aNode_array[0])
        UsedEdges_set = set()
        for AnEdge_array in self.EdgeIndex_array:
            if (AnEdge_array[0], AnEdge_array[1]) not in UsedEdges_set:
                self.TheGraph_graph.add_edge(AnEdge_array[0], AnEdge_array[1])
            UsedEdges_set.add((AnEdge_array[0], AnEdge_array[1]))

    def add_labels(self, LabelName_str, Labels_npArray):
        '''Adds labeling data to the nodes in self.TheGraph_graph.
        '''
        
        
        UsedClusters_set = set()
        for aNode_array in self.NodeIndex_array:
            if aNode_array[0] not in UsedClusters_set:
                self.TheGraph_graph.node[aNode_array[0]][LabelName_str] = \
                str(Labels_npArray[
                        self.FilteredPointCloud_npArray[aNode_array[1], 0]])
            else:
                self.TheGraph_graph.node[aNode_array[0]][LabelName_str] = \
                self.TheGraph_graph.node[aNode_array[0]][LabelName_str] + \
                ', ' + str(Labels_npArray[
                        self.FilteredPointCloud_npArray[aNode_array[1], 0]])
            UsedClusters_set.add(aNode_array[0])
                
    def add_mean_properties(self, PropertiesName_str, Properties_npArray):
        '''Adds meaned properties to the nodes in the graph.
        '''
        
        
        UsedClusters_set = set()
        for aNode_array in self.NodeIndex_array:
            if aNode_array[0] not in UsedClusters_set:
                self.TheGraph_graph.node[aNode_array[0]][PropertiesName_str] =\
                float(Properties_npArray[
                self.FilteredPointCloud_npArray[aNode_array[1], 0]])
            else:
                self.TheGraph_graph.node[aNode_array[0]][PropertiesName_str] =\
                self.TheGraph_graph.node[aNode_array[0]][PropertiesName_str] +\
                float(Properties_npArray[
                self.FilteredPointCloud_npArray[aNode_array[1], 0]])
            UsedClusters_set.add(aNode_array[0])
        
        for aNode_int in self.TheGraph_graph:
            self.TheGraph_graph.node[aNode_int][PropertiesName_str] = \
            self.TheGraph_graph.node[aNode_int][PropertiesName_str] / \
            float(self.TheGraph_graph.node[aNode_int]['NumberOfPoints'])
            
    def add_summed_properties(self, PropertiesName_str, Properties_npArray):
        '''Adds summed properties to the nodes in the graph.
        '''
        
        
        UsedClusters_set = set()
        for aNode_array in self.NodeIndex_array:
            if aNode_array[0] not in UsedClusters_set:
                self.TheGraph_graph.node[aNode_array[0]][PropertiesName_str] =\
                float(Properties_npArray[
                self.FilteredPointCloud_npArray[aNode_array[1], 0]])
            else:
                self.TheGraph_graph.node[aNode_array[0]][PropertiesName_str] =\
                self.TheGraph_graph.node[aNode_array[0]][PropertiesName_str] +\
                float(Properties_npArray[
                self.FilteredPointCloud_npArray[aNode_array[1], 0]])
            UsedClusters_set.add(aNode_array[0])




