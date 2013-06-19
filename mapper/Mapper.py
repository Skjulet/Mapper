'''Mapper.py is the main object that executes the mapper algorithm and
distributes the steps in the algorithm to several other classes (the ones
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
    def __init__(self, PointCloud_npArray, Metric_me, Lens_str, BINS_int,
                OVERLAP_flt, Clust_str, EPS_flt, DebugMode_bol = False):
        '''The Mapper object is initiated with a set PointCloud_npArray and
        dependes on several other variables (see above)
        '''


        self.DebugMode_bol = DebugMode_bol
        if self.DebugMode_bol == True:
            print("In Mapper__init__: Mapper is now running in debug mode")	
            print()	


        self.PointCloud_npArray = PointCloud_npArray

        self.Metric_me = me.Metric(Metric_me,self.DebugMode_bol)

        self.Equalize_bol = True
        self.OVERLAP_flt = OVERLAP_flt
        self.BINS_int = bi.Bins(BINS_int, self.OVERLAP_flt,
                                self.Equalize_bol, self.DebugMode_bol)	
        self.Lens_str = le.Lens(Lens_str, self.Metric_me,
                                self.BINS_int, DebugMode_bol)

        self.EPS_flt = EPS_flt
        self.Clust_str = cl.Clust(self.PointCloud_npArray, 
                                Clust_str, self.EPS_flt, 
                                self.Metric_me, self.DebugMode_bol)

        self.Coloring_npArray = None
        self.GrapherObject_gr = None
        self.properties = None
        self.Labels_npArray = None

        #Filters cloud on the lenses filter
        self.filteredcloud = self.Lens_str.filtered(self.PointCloud_npArray)
        if self.DebugMode_bol == True:
             print("In Mapper__init__: Printing self.filteredcloud in the\
             Mapper object:")
             print(self.filteredcloud)	

        #clusters the cloud
        self.clusteredcloud = \
        self.Clust_str.TESTmakeclustering(self.filteredcloud)


        if self.DebugMode_bol == True:
            print("In Mapper__init__: Printing self.clusteredcloud:")
            print(self.clusteredcloud)


        #creates a graph from the self.PointCloud_npArray and clustering data
        self.GrapherObject_gr = gr.Grapher(self.PointCloud_npArray, 
                                    self.clusteredcloud, self.DebugMode_bol)
        self.GrapherObject_gr.makegraph()

    def mmetric(self, Metric_me):
        '''Function that modifies the self.Metric_me object
        '''


        self.Metric_me = me.Metric(Metric_me, self.DebugMode_bol)

    def mlens(self, Lens_str):
        '''Function that modifies the self.Lens_str object
        '''


        self.Lens_str = le.Lens(Lens_str, self.Metric_me,
                                self.BINS_int, self.DebugMode_bol)

    def moverlap(self, OVERLAP_flt):
        '''Function that modifies the self.OVERLAP_flt object
        '''


        self.OVERLAP_flt = OVERLAP_flt

    def mbins(self, BINS_int):
        '''Function that modifies the self.BINS_int object
        '''


        self.BINS_int = BINS_int

    def mclust(self, Clust_str):
        '''Function that modifies the self.Clust_str object
        '''


        self.Clust_str = cl.Clust(self.PointCloud_npArray, Clust_str,
                                self.Metric_me, self.DebugMode_bol)

    def addlabels(self, Labels_npArray):
        '''Function that adds Labels_npArray to the graph in
        self.GrapherObject_gr
        '''


        self.Labels_npArray = Labels_npArray
        self.GrapherObject_gr.addlabels(self.Labels_npArray)
        G = self.GrapherObject_gr.GetGraph()
        print(G.nodes(data=True)[0])
        print(G.edges(data=True)[0:5])

    def AddFilterToGraph(self):
        '''Function that adds meaned filter values to the nodes in the graph
        in self.GrapherObject_gr
        '''


        pass

    def addproperties(self, properties, PropertiesName_str):
        '''Function that adds meaned properties values to the nodes in the
        graph in self.GrapherObject_gr
        '''


        self.properties = np.column_stack((self.properties, properties))

    def visualize(self):
        '''This function saves the graph in a map in .graphml format
        '''


        pass
	#nx.write_graphml(self.GrapherObject_gr.GetGraph(), 'graph_files/' +\
	#'TestGraph' + '.graphml')







