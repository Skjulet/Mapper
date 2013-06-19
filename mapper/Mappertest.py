'''This is a test program that we use to develop the mapper algorithm
'''
import numpy as np

import Mapper as ma




WordData_npArray = np.load('../../Mapper_Data_Files/\
npy_files/easygoing_neighbors.npy')
LabelData_npArray = np.load('../../Mapper_Data_Files/\
npy_files/easygoing_neighborswords.npy')
Cloud_npArray = WordData_npArray

Metric_str = 'cosine'
Lens_str = 'Semantic'
BINS_int = 5
OVERLAP_flt = 0.9
Clust_str = 'CompleteLinkage'
EPS_flt = 0.92


testobjekt_ma = ma.Mapper(Cloud_npArray,Metric_str,Lens_str,BINS_int,
    OVERLAP_flt,Clust_str,EPS_flt,DebugMode_bol = False)

testobjekt_ma.addlabels(LabelData_npArray)

#testobjekt.visualize()

