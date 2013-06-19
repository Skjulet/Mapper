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
    def __init__(self,PointCloud_npArray,Metric_me,Lens_str,BINS_int,
                OVERLAP_flt,Clust_str,EPS_flt,DebugMode_bol = False):
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
        self.BINS_int = bi.Bins(BINS_int, self.OVERLAP_flt, self.Equalize_bol, self.DebugMode_bol)	
        self.Lens_str = le.Lens(Lens_str,self.Metric_me,self.BINS_int,DebugMode_bol)

        self.EPS_flt = EPS_flt
        self.Clust_str = cl.Clust(self.PointCloud_npArray,Clust_str,self.EPS_flt,self.Metric_me,self.DebugMode_bol)

        self.coloring = None
        self.grapherobject = None
        self.properties = None
        self.labels = None

        #Filters cloud on the lenses filter
        self.filteredcloud = self.Lens_str.filtered(self.PointCloud_npArray)
        if self.DebugMode_bol == True:
             print("In Mapper__init__: Printing self.filteredcloud in the Mapper object:")
             print(self.filteredcloud)	

        #clusters the cloud
        self.clusteredcloud = self.Clust_str.TESTmakeclustering(self.filteredcloud)


        if self.DebugMode_bol == True:
            print("In Mapper__init__: Printing self.clusteredcloud:")
            print(self.clusteredcloud)


        #creates a graph from the self.PointCloud_npArray and clustering data
        self.grapherobject = gr.Grapher(self.PointCloud_npArray,self.clusteredcloud,self.DebugMode_bol)
        self.grapherobject.makegraph()

    def mmetric(self,Metric_me):
        '''
        '''


        self.Metric_me = me.Metric(Metric_me,self.DebugMode_bol)

    def mlens(self, Lens_str):
        '''
        '''


        self.Lens_str = le.Lens(Lens_str,self.Metric_me,self.BINS_int,self.DebugMode_bol)

    def moverlap(self,OVERLAP_flt):
        '''
        '''


        self.OVERLAP_flt = OVERLAP_flt

    def mbins(self,BINS_int):
        '''
        '''


        self.BINS_int = BINS_int

    def mclust(self,Clust_str):
        '''
        '''


        self.Clust_str = cl.Clust(PointCloud_npArray,Clust_str,self.Metric_me,self.DebugMode_bol)

    def addlabels(self,labels):
        '''
        '''


        self.labels = labels
        self.grapherobject.addlabels(self.labels)
        G = self.grapherobject.GetGraph()
        print(G.nodes(data=True)[0])
        print(G.edges(data=True)[0:5])

    def AddFilterToGraph(self):
        '''
        '''


        pass

    def addproperties(self,properties,PropertiesName):
        '''
        '''


        self.properties = np.column_stack((self.properties, properties))

    #This function saves the graph in graph_files/ in .graphml format
    def visualize(self):
        '''
        '''


        pass
	#nx.write_graphml(self.grapherobject.GetGraph(), 'graph_files/' + 'TestGraph' + '.graphml')







