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
from Filter_Functions import FilterFunctions as ff


class Mapper:
    def __init__(self,
                PointCloud_npArray=None,
                MetricName_str=None,
                LensName_str=None,
                LensArguments_array=None,
                BINNUMBER_int=None,
                OVERLAP_flt=None,
                ClusterAlgorithm_str=None,
                ClusterArguments_array=None,
                DebugMode_bol=None):
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
        
        self.UnsortedFilterValues_npArray = None
        self.PointCloudDistanceMatrix_npArray = None
        
        self.CheckList_list = None
        self.IsAnalysed_bol = False
        
        if self.DebugMode_bol == True:
            print("In Mapper__init__: Mapper is now running in debug mode")
            print()	
            
        self.Equalize_bol = True

        self.Coloring_npArray = None
        self.GrapherObject_gr = None
        self.Properties_dict = {}
        self.FilterAdded_ToGraphbol = True
        self.LabelName_str = None
        self.Labels_npArray = None
        
        self.MetricObject_me = None
        self.BinsObjebt_bi = None
        self.LensObject_le = None
        self.ClustObject_cl = None
        self.GrapherObject_gr = None
        
        self.FilteredPointCloud_npArray = None
        self.Binning_array = None
        self.Clustering_array = None
        self.ClusteredPointCloud_npArray = None

    def analyse(self):
        '''A function that executes the mapper algorithm when all 
        the required parameters are given.  '''
        
        
        self.CheckList_list = [int(self.PointCloud_npArray is None),
                                int(self.MetricName_str is None),
                                int(self.LensName_str is None),
                                int(self.LensArguments_array is None),
                                int(self.BINNUMBER_int is None),
                                int(self.OVERLAP_flt is None),
                                int(self.ClusterAlgorithm_str is None),
                                int(self.ClusterArguments_array is None)]
        if sum(self.CheckList_list) == 0 and self.IsAnalysed_bol == False:
            #Initiates required objects.
            self.MetricObject_me = me.Metric(self.MetricName_str, 
                                        self)
            self.BinsObjebt_bi = bi.Bins(self.BINNUMBER_int,
                                        self.OVERLAP_flt,
                                        self.Equalize_bol,
                                        self)
            self.LensObject_le = le.Lens(self.LensName_str,
                                        self.LensArguments_array,
                                        self.MetricObject_me,
                                        self.BinsObjebt_bi,
                                        self)
            self.ClustObject_cl = cl.Clust(self.PointCloud_npArray, 
                                        self.ClusterAlgorithm_str,
                                        self.ClusterArguments_array, 
                                        self.MetricObject_me,
                                        self)
                                    
            #Bins and filters cloud on the lenses filter.
            [self.FilteredPointCloud_npArray, self.Binning_array]= \
            self.LensObject_le.filter_point_cloud(self.PointCloud_npArray)
            if self.DebugMode_bol == True:
                 print("In Mapper.analyse(): Printing self.BFPointCloud_npArray\
                 in the Mapper object:")
                 print(self.BFPointCloud_npArray)	

            #Clusters the cloud.
            self.Clustering_array = self.ClustObject_cl.create_clustering(
                                            self.FilteredPointCloud_npArray,
                                            self.Binning_array)

            if self.DebugMode_bol == True:
                print("In Mapper.analyse(): Printing\
                self.ClusteredPointCloud_npArray:")
                print(self.ClusteredPointCloud_npArray)

            #Creates a graph from the self.PointCloud_npArray and
            #clustering data.
            self.GrapherObject_gr = gr.Grapher(self.PointCloud_npArray, 
                                        self.Clustering_array,
                                        self)
            
            if self.LabelName_str != None and self.Labels_npArray != None:
                self.GrapherObject_gr.add_labels(self.LabelName_str,
                                            self.Labels_npArray)
            if self.Properties_dict != {}:
                for Property_str in self.Properties_dict:
                    self.GrapherObject_gr.add_mean_properties(Property_str, 
                                            self.Properties_dict[Property_str])
            self.IsAnalysed_bol = True
        
    def configure(self,
                PointCloud_npArray=None,
                MetricName_str=None,
                LensName_str=None,
                LensArguments_array=None,
                BINNUMBER_int=None,
                OVERLAP_flt=None,
                ClusterAlgorithm_str=None,
                ClusterArguments_array=None,
                DebugMode_bol=None):
        '''A function that adds or changes configurations in the mapper
        object.  '''
        
        if PointCloud_npArray != None:
            self.PointCloud_npArray = PointCloud_npArray
        if MetricName_str != None:
            self.MetricName_str = MetricName_str
        if LensName_str != None:
            self.LensName_str = LensName_str
        if LensArguments_array != None:
            self.LensArguments_array = LensArguments_array
        if BINNUMBER_int != None:
            self.BINNUMBER_int = BINNUMBER_int
        if OVERLAP_flt != None:
            self.OVERLAP_flt = OVERLAP_flt
        if ClusterAlgorithm_str != None:
            self.ClusterAlgorithm_str = ClusterAlgorithm_str
        if ClusterArguments_array != None:
            self.ClusterArguments_array = ClusterArguments_array
        if DebugMode_bol != None:
            self.DebugMode_bol = DebugMode_bol
        
    def add_labels(self, LabelName_str, Labels_npArray):
        '''Function that adds Labels_npArray to the graph in
        self.GrapherObject_gr.  '''


        self.LabelName_str = LabelName_str
        self.Labels_npArray = Labels_npArray
        if self.IsAnalysed_bol == True:
            self.GrapherObject_gr.add_labels(self.LabelName_str,
                                            self.Labels_npArray)
    
    def add_filter_to_graph(self):
        '''Function that adds meaned filter values to the nodes in the
        graph in self.GrapherObject_gr.  '''

        if self.IsAnalysed_bol == True:
            self.add_mean_properties('Filter Value', 
                                    self.UnsortedFilterValues_npArray)
        self.FilterAddedToGraph_bol = True

    def add_mean_properties(self, PropertiesName_str, Properties_npArray):
        '''Function that adds meaned properties values to the nodes in
        the graph in self.GrapherObject_gr.  '''

        
        self.Properties_dict[PropertiesName_str] = Properties_npArray
        if self.IsAnalysed_bol == True:
            self.GrapherObject_gr.add_mean_properties(PropertiesName_str, 
                                                    Properties_npArray)

    def save_configurations(self, DirectoryPath_str, FileName_str):
        '''A function that saves configuration to a file in a given
        locantion.  '''
        
        
        with open(DirectoryPath_str + FileName_str + '.pk', 'wb') as output:
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
        
    def load_configurations(self, DirectoryPath_str, FileName_str):
        '''A function that loads a configuration file, created with 
        save_configurations, from a given locantion.  '''
        
        
        with open(DirectoryPath_str + FileName_str + '.pk', 'rb') as input:
            self.MetricName_str = pickle.load(input)
            self.LensName_str = pickle.load(input)
            self.LensArguments_array = pickle.load(input)
            self.BINNUMBER_int = pickle.load(input)
            self.OVERLAP_flt = pickle.load(input)
            self.ClusterAlgorithm_str = pickle.load(input)
            self.ClusterArguments_array = pickle.load(input)    
        
    def save_filter_values(self, DirectoryPath_str, FileName_str):
        '''A function that saves filter values, sorted in the same
        order as the initial PointCloud_npArray, to a file on a 
        given locantion.  '''
        
        
        with open(DirectoryPath_str + FileName_str + '.pk', 'wb') as output:
            if self.UnsortedFilterValues_npArray != None:
                pickle.dump(self.UnsortedFilterValues_npArray, output,
                            pickle.HIGHEST_PROTOCOL)
            else:
                self.UnsortedFilterValues_npArray = \
                ff.FilterFunctions().apply_filter(self.PointCloud_npArray,
                                                me.Metric(self.MetricName_str, 
                                                        self), 
                                                self.LensName_str, 
                                                self.LensArguments_array)
                pickle.dump(self.UnsortedFilterValues_npArray, output,
                            pickle.HIGHEST_PROTOCOL)
                            
    def load_filter_values(self, DirectoryPath_str, FileName_str):
        '''A function that loads filter values, sorted in the same
        order as the initial PointCloud_npArray, to a file on a 
        given locantion.  '''
        
        with open(DirectoryPath_str + FileName_str + '.pk', 'rb') as input:
            self.UnsortedFilterValues_npArray = pickle.load(input)
        
    def save_graph(self, DirectoryPath_str, FileName_str):
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





