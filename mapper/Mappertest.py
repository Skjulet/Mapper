'''This is a test program that we use to develop the mapper algorithm
'''


import numpy as np

import Mapper as ma


WordData_npArray = np.load('../../Mapper_Data_Files/\
npy_files/easygoing_neighbors.npy')
LabelData_npArray = np.load('../../Mapper_Data_Files/\
npy_files/easygoing_neighborswords.npy')
Cloud_npArray = WordData_npArray

MetricName_str = 'cosine'
LensName_str = 'Semantic'
LensArguments_array = []
BINS_int = 5
OVERLAP_flt = 0.9
Clust_str = 'CompleteLinkage'
ClusterArguments_array = [0.92]    #The epsilon value

testobject_ma = ma.Mapper(Cloud_npArray, MetricName_str, LensName_str, 
    LensArguments_array, BINS_int, OVERLAP_flt, Clust_str, 
    ClusterArguments_array, DebugMode_bol = False)
testobject_ma.add_labels('Labels', LabelData_npArray)
testobject_ma.add_filter_to_graph()

testobject_ma.print_graph()
#testobject_ma.save_file_to_map()

