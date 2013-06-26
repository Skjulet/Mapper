'''Mapper.py is the main object that executes the mapper algorithm and
distributes the steps in the algorithm to several other classes the 
ones imported last.  '''


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
        '''The Mapper object is initiated with a set PointCloud_npArray
        and dependes on several other variables (see above).  '''


        self.DebugMode_bol = DebugMode_bol
        if self.DebugMode_bol == True:
            print("In Mapper__init__: Mapper is now running in debug mode")
            print()	

        self.PointCloud_npArray = PointCloud_npArray

        self.MetricObject_me = me.Metric(MetricName_str, self.DebugMode_bol)

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
        self.Properties_dict = {}
        self.LabelName_str = None
        self.Labels_npArray = None

        #Bins and filters cloud on the lenses filter.
        self.BFPointCloud_npArray = \
        self.LensObject_le.filter_point_cloud(self.PointCloud_npArray)
        if self.DebugMode_bol == True:
             print("In Mapper__init__: Printing self.BFPointCloud_npArray in\
             the Mapper object:")
             print(self.BFPointCloud_npArray)	

        #Clusters the cloud.
        self.ClusteredPointCloud_npArray = \
        self.ClustObject_cl.create_clustering(self.BFPointCloud_npArray)

        if self.DebugMode_bol == True:
            print("In Mapper__init__: Printing\
            self.ClusteredPointCloud_npArray:")
            print(self.ClusteredPointCloud_npArray)

        #Creates a graph from the self.PointCloud_npArray and
        #clustering data.
        self.GrapherObject_gr = gr.Grapher(self.PointCloud_npArray, 
                                    self.ClusteredPointCloud_npArray,
                                    self.DebugMode_bol)
    
    def change_metric(self, MetricName_str):
        '''Function that modifies the self.MetricObject_me object
        '''


        self.MetricObject_me = me.Metric(MetricName_str, self.DebugMode_bol)

    def change_lens(self, LensName_str):
        '''Function that modifies the self.LensObject_le object
        '''


        self.LensObject_le = le.Lens(LensName_str, self.MetricObject_me,
                                self.BinsObjebt_bi, self.DebugMode_bol)

    def change_overlap(self, OVERLAP_flt):
        '''Function that modifies the self.OVERLAP_flt object
        '''


        self.OVERLAP_flt = OVERLAP_flt

    def change_bin_number(self, BINNUMBER_int):
        '''Function that modifies the self.BinsObjebt_bi object
        '''


        self.BinsObjebt_bi = BINNUMBER_int

    def change_clust_alg(self, ClusterAlgorithm_str):
        '''Function that modifies the self.ClustObject_cl object.  
        '''


        self.ClustObject_cl = cl.Clust(self.PointCloud_npArray, 
                                ClusterAlgorithm_str, self.MetricObject_me,
                                self.DebugMode_bol)

    def add_labels(self, LabelName_str, Labels_npArray):
        '''Function that adds Labels_npArray to the graph in
        self.GrapherObject_gr.  '''


        self.LabelName_str = LabelName_str
        self.Labels_npArray = Labels_npArray
        self.GrapherObject_gr.add_labels(LabelName_str, self.Labels_npArray)
        
    def add_filter_to_graph(self):
        '''Function that adds meaned filter values to the nodes in the
        graph in self.GrapherObject_gr.  '''


        self.add_mean_properties('Filter Value', 
                                self.BFPointCloud_npArray[:, 1])

    def add_mean_properties(self, PropertiesName_str, Properties_npArray):
        '''Function that adds meaned properties values to the nodes in
        the graph in self.GrapherObject_gr.  '''

        
        self.Properties_dict[PropertiesName_str] = Properties_npArray
        self.GrapherObject_gr.add_mean_properties(PropertiesName_str, 
                                                    Properties_npArray)
        
    def save_file_to_map(self, DirectoryPath_str, FileName_str):
        '''This function saves the graph in a map in .graphml format.  
        '''


        pass
        #nx.write_graphml(self.GrapherObject_gr.get_graph(),
        #DirectoryPath_str + FileName_str + '.graphml')

    def print_graph(self):
        '''Prints a portion of the graph specified in the code below.
        '''
        
        test_graph = self.GrapherObject_gr.get_graph()
        print(test_graph.nodes(data=True)[0])
        print(test_graph.edges(data=True)[0:5])





