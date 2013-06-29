'''Mapper.py is the main object that executes the mapper algorithm and
distributes the steps in the algorithm to several other classes the 
ones imported last.  '''


import numpy as np

import networkx as nx
import pickle

import Metric as me
import Lens as le
import Bins as bi
import Clust as cl
import Grapher as gr


class Mapper:
    def __init__(self,
                PointCloud_npArray = None,
                MetricName_str = None,
                LensName_str = None,
                LensArguments_array = None,
                BINNUMBER_int = None,
                OVERLAP_flt = None,
                ClusterAlgorithm_str = None,
                ClusterArguments_array = None,
                DebugMode_bol = None):
        '''The Mapper object is initiated with a set PointCloud_npArray
        and dependes on several other variables (see above).  '''
        
        
        self.PointCloud_npArray = PointCloud_npArray
        self.MetricName_str = MetricName_str
        self.LensName_str = LensName_str
        self.LensArguments_array = LensArguments_array
        self.BINNUMBER_int = BINNUMBER_int
        self.OVERLAP_flt = OVERLAP_flt
        self.ClusterAlgorithm_str = ClusterAlgorithm_str
        self.ClusterArguments_array = ClusterArguments_array
        self.DebugMode_bol = DebugMode_bol
        
        self.checklist_list = None
        
        if self.DebugMode_bol == True:
            print("In Mapper__init__: Mapper is now running in debug mode")
            print()	
            
        self.Equalize_bol = True

        self.Coloring_npArray = None
        self.GrapherObject_gr = None
        self.Properties_dict = {}
        self.LabelName_str = None
        self.Labels_npArray = None
        
        self.MetricObject_me = None
        self.BinsObjebt_bi = None
        self.LensObject_le = None
        self.ClustObject_cl = None
        self.GrapherObject_gr = None
        
        self.BFPointCloud_npArray = None
        self.ClusteredPointCloud_npArray = None
        
        self.analyse()
        
    def analyse(self):
        '''A function that executes the mapper algorithm when all 
        the required parameters are given.  '''
        
        
        self.checklist_list = [int(self.PointCloud_npArray is None),
                                int(self.MetricName_str is None),
                                int(self.LensName_str is None),
                                int(self.LensArguments_array is None),
                                int(self.BINNUMBER_int is None),
                                int(self.OVERLAP_flt is None),
                                int(self.ClusterAlgorithm_str is None),
                                int(self.ClusterArguments_array is None),
                                int(self.DebugMode_bol is None)]
        if sum(self.checklist_list) == 0:
            #Initiates required objects.
            self.MetricObject_me = me.Metric(self.MetricName_str, 
                                        self.DebugMode_bol)
            self.BinsObjebt_bi = bi.Bins(self.BINNUMBER_int, 
                                        self.OVERLAP_flt,
                                        self.Equalize_bol,
                                        self.DebugMode_bol)	
            self.LensObject_le = le.Lens(self.LensName_str, 
                                        self.LensArguments_array,
                                        self.MetricObject_me, 
                                        self.BinsObjebt_bi,
                                        self.DebugMode_bol)
            self.ClustObject_cl = cl.Clust(self.PointCloud_npArray, 
                                        self.ClusterAlgorithm_str,
                                        self.ClusterArguments_array, 
                                        self.MetricObject_me,
                                        self.DebugMode_bol)
                                    
            #Bins and filters cloud on the lenses filter.
            self.BFPointCloud_npArray = \
            self.LensObject_le.filter_point_cloud(self.PointCloud_npArray)
            if self.DebugMode_bol == True:
                 print("In Mapper.analyse(): Printing self.BFPointCloud_npArray\
                 in the Mapper object:")
                 print(self.BFPointCloud_npArray)	

            #Clusters the cloud.
            self.ClusteredPointCloud_npArray = \
            self.ClustObject_cl.create_clustering(self.BFPointCloud_npArray)

            if self.DebugMode_bol == True:
                print("In Mapper.analyse(): Printing\
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

    def save_configurations(self, DirectoryPath_str, FileName_str):
        '''A function that saves configuration to a file in a given
        locantion.  '''
        
        
        with open(DirectoryPath_str + FileName_str + '.pk', 'wb') as output:
            pickle.dump(self.PointCloud_npArray, output,
                        pickle.HIGHEST_PROTOCOL)
            pickle.dump(self.MetricName_str, output, pickle.HIGHEST_PROTOCOL)
            pickle.dump(self.LensName_str, output, pickle.HIGHEST_PROTOCOL)
            pickle.dump(self.LensArguments_array, output,
                        pickle.HIGHEST_PROTOCOL)
            pickle.dump(self.BINNUMBER_int, output, pickle.HIGHEST_PROTOCOL)
            pickle.dump(self.OVERLAP_flt, output, pickle.HIGHEST_PROTOCOL)
            pickle.dump(self.ClusterAlgorithm_str, output,
                        pickle.HIGHEST_PROTOCOL)
            pickle.dump(self.ClusterArguments_array, output,
                        pickle.HIGHEST_PROTOCOL)
            pickle.dump(self.DebugMode_bol, output, pickle.HIGHEST_PROTOCOL)
        
    def load_configurations(self, DirectoryPath_str, FileName_str):
        '''A function that loads a configuration file, created with 
        save_configurations, from a given locantion.  '''
        
        
        with open(DirectoryPath_str + FileName_str + '.pk', 'rb') as input:
            self.PointCloud_npArray = pickle.load(input)
            self.MetricName_str = pickle.load(input)
            self.LensName_str = pickle.load(input)
            self.LensArguments_array = pickle.load(input)
            self.BINNUMBER_int = pickle.load(input)
            self.OVERLAP_flt = pickle.load(input)
            self.ClusterAlgorithm_str = pickle.load(input)
            self.ClusterArguments_array = pickle.load(input)
            self.DebugMode_bol = pickle.load(input)    
        self.analyse()
        
    def save_file_to_map(self, DirectoryPath_str, FileName_str):
        '''This function saves the graph in a map in .graphml format.
        '''


        nx.write_graphml(self.GrapherObject_gr.get_graph(),
        DirectoryPath_str + FileName_str + '.graphml')

    def print_graph(self):
        '''Prints a portion of the graph specified in the code below.
        '''
        
        test_graph = self.GrapherObject_gr.get_graph()
        print(test_graph.nodes(data=True)[0])
        print(test_graph.edges(data=True)[0:5])





