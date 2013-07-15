'''This is a test program that we use to develop the mapper algorithm.
'''


import numpy as np

import Mapper as ma


WordData_npArray = np.load('../../Mapper_Data_Files/\
npy_files/Synonyms/synonyms1Vectors.npy')
LabelData_npArray = np.load('../../Mapper_Data_Files/\
npy_files/Synonyms/synonyms1Words.npy')

Cloud_npArray = WordData_npArray

MetricName_str = 'cosine'
LensName_str = 'nth_neighbor'
LensArguments_array = []
Equalize_bol = True
BINS_int = 4
OVERLAP_flt = 0.9
Clust_str = 'CompleteLinkage'
ClusterArguments_array = [1]    #The epsilon value

RightWrong_npArray = np.load('../../Mapper_Data_Files/filter_files/\
Synonyms/rightwrongfilter.npy')

while BINS_int < 21:
    
    TestObject_ma = ma.Mapper(Cloud_npArray, MetricName_str, LensName_str,
        LensArguments_array, Equalize_bol, BINS_int, OVERLAP_flt, Clust_str,
        ClusterArguments_array, DebugMode_bol = False)
    #TestObject_ma.save_filter_values('../../Mapper_Data_Files/filter_files/',
    # 'easygoing_neighborsfilters')

    
    TestObject_ma.add_mean_properties('RightWrong', RightWrong_npArray)

    TestObject_ma.load_filter_values('../../Mapper_Data_Files/filter_files/Synonyms/', 'SynonymsAverageFilter')


    TestObject_ma.add_filter_to_graph()
    TestObject_ma.add_labels('Labels', LabelData_npArray)

    TestObject_ma.analyse()

    TestObject_ma.save_graph('../../Mapper_Data_Files/graph_files/',
                                'synonymsAverageBins' + str(BINS_int))
    BINS_int =  BINS_int + 2

#TestObject_ma.save_configurations(
# '../../Mapper_Data_Files/config_files/','synonymsAverage')

#TestObject_ma.print_graph()
#TestObject_ma.save_graph('../../Mapper_Data_Files/graph_files/',
#                            'Testfile_master')

