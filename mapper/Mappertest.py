'''This is a test program that we use to develop the mapper algorithm
TESTING NEW BRANCH
'''


import numpy as np

import Mapper as ma


WordData_npArray = np.load('../../Mapper_Data_Files/\
npy_files/easygoing_neighbors.npy')
LabelData_npArray = np.load('../../Mapper_Data_Files/\
npy_files/easygoing_neighborswords.npy')

Cloud_npArray = WordData_npArray

MetricName_str = 'euclidean'
LensName_str = 'nth_neighbor'
LensArguments_array = []
BINS_int = 5
OVERLAP_flt = 0.9
Clust_str = 'CompleteLinkage'
ClusterArguments_array = [0.92]    #The epsilon value

#TestObjectTwo_ma = ma.Mapper()

TestObject_ma = ma.Mapper(Cloud_npArray, MetricName_str, LensName_str, 
    LensArguments_array, BINS_int, OVERLAP_flt, Clust_str, 
    ClusterArguments_array, DebugMode_bol = False)
TestObject_ma.save_filter_values('../../Mapper_Data_Files/filter_files/',
                                'easygoing_neighborsfilters')
                                
#TestObject_ma.load_filter_values('../../Mapper_Data_Files/filter_files/',
#                                'easygoing_neighborsfilters')
TestObject_ma.add_labels('Labels', LabelData_npArray)

TestObject_ma.add_filter_to_graph()
TestObject_ma.analyse()

#TestObject_ma.save_file_to_map(
#                        '../../Mapper_Data_Files/graph_files/', 'bnc_food')

#TestObject_ma.save_configurations(
#                        '../../Mapper_Data_Files/config_files/','Testfile')

TestObject_ma.print_graph()

#TestObject_ma.print_graph()
#TestObject_ma.save_graph()
