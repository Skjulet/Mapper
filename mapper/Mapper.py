'''Mapper.py is the main object that executes the mapper algorithm and
distributes the steps in the algorithm to several other classes the ones
imported last.
'''
import numpy as np

import networkx as nx

import Metric as me
import Lens as le
import Bins as bi
import Clust as cl
import Grapher as gr


class Mapper:
    def __init__(self, PointCloud_npArray, MetricName_str, LensName_str,
                BINNUMBER_int, OVERLAP_flt, ClusterAlgorithm_str,
                EPS_flt, DebugMode_bol = False):
        '''The Mapper object is initiated with a set PointCloud_npArray and
        dependes on several other variables (see above)
        '''


        self.DebugMode_bol = DebugMode_bol
        if self.DebugMode_bol == True:
            print("In Mapper__init__: Mapper is now running in debug mode")
            print()	


        self.PointCloud_npArray = PointCloud_npArray

        self.MetricObject_me = me.Metric(MetricName_str,self.DebugMode_bol)

        self.Equalize_bol = True
        self.OVERLAP_flt = OVERLAP_flt
        self.BinsObjebt_bi = bi.Bins(BINNUMBER_int, self.OVERLAP_flt,
                                self.Equalize_bol, self.DebugMode_bol)	
        self.LensObject_le = le.Lens(LensName_str, self.MetricObject_me,
                                self.BinsObjebt_bi, DebugMode_bol)

        self.EPS_flt = EPS_flt
        self.ClustObject_cl = cl.Clust(self.PointCloud_npArray, 
                                ClusterAlgorithm_str, self.EPS_flt, 
                                self.MetricObject_me, self.DebugMode_bol)

        self.Coloring_npArray = None
        self.GrapherObject_gr = None
        self.Properties_dict = None
        self.Labels_npArray = None

        #Bins and filters cloud on the lenses filter
        self.BFPointCloud_npArray = \
        self.LensObject_le.filtered(self.PointCloud_npArray)
        if self.DebugMode_bol == True:
             print("In Mapper__init__: Printing self.BFPointCloud_npArray in\
             the Mapper object:")
             print(self.BFPointCloud_npArray)	

        #clusters the cloud
        self.ClusteredPointCloud_npArray = \
        self.ClustObject_cl.TESTmakeclustering(self.BFPointCloud_npArray)


        if self.DebugMode_bol == True:
            print("In Mapper__init__: Printing\
            self.ClusteredPointCloud_npArray:")
            print(self.ClusteredPointCloud_npArray)


        #creates a graph from the self.PointCloud_npArray and clustering data
        self.GrapherObject_gr = gr.Grapher(self.PointCloud_npArray, 
                                    self.ClusteredPointCloud_npArray,
                                    self.DebugMode_bol)
        self.GrapherObject_gr.makegraph()

    def mmetric(self, MetricName_str):
        '''Function that modifies the self.MetricObject_me object
        '''


        self.MetricObject_me = me.Metric(MetricName_str, self.DebugMode_bol)

    def mlens(self, LensName_str):
        '''Function that modifies the self.LensObject_le object
        '''


        self.LensObject_le = le.Lens(LensName_str, self.MetricObject_me,
                                self.BinsObjebt_bi, self.DebugMode_bol)

    def moverlap(self, OVERLAP_flt):
        '''Function that modifies the self.OVERLAP_flt object
        '''


        self.OVERLAP_flt = OVERLAP_flt

    def mbins(self, BINNUMBER_int):
        '''Function that modifies the self.BinsObjebt_bi object
        '''


        self.BinsObjebt_bi = BINNUMBER_int

    def mclust(self, ClusterAlgorithm_str):
        '''Function that modifies the self.ClustObject_cl object
        '''


        self.ClustObject_cl = cl.Clust(self.PointCloud_npArray, 
                                ClusterAlgorithm_str, self.MetricObject_me,
                                self.DebugMode_bol)

    def addlabels(self, Labels_npArray):
        '''Function that adds Labels_npArray to the graph in
        self.GrapherObject_gr
        '''


        self.Labels_npArray = Labels_npArray
        self.GrapherObject_gr.addlabels(self.Labels_npArray)
        G_graph = self.GrapherObject_gr.GetGraph()
        print(G_graph.nodes(data=True)[0])
        print(G_graph.edges(data=True)[0:5])

    def AddFilterToGraph(self):
        '''Function that adds meaned filter values to the nodes in the graph
        in self.GrapherObject_gr
        '''


        pass

    def addproperties(self, Properties_npArray, PropertiesName_str):
        '''Function that adds meaned properties values to the nodes in the
        graph in self.GrapherObject_gr
        '''


        self.Properties_dict = np.column_stack((self.Properties_dict,
                                                Properties_npArray))

    def visualize(self, DirectoryPath_str, FileName_str):
        '''This function saves the graph in a map in .graphml format
        '''


        pass
	#nx.write_graphml(self.GrapherObject_gr.GetGraph(), DirectoryPath_str +\
	#FileName_str + '.graphml')







