''' The lens class applies the chosen lens to the point cloud data.
'''
import numpy as np
import Metric as me
import Filters as fi

class Lens:
    def __init__(self, LensName_str, Metric_me, BinObject_be,
                 DebugMode_bol=False):
        '''The Lens object is initiated with a set with four arguments.
        '''
        
        
        self.DebugMode_bol = DebugMode_bol
        
        self.LensName_str = LensName_str
        self.Metric_me = Metric_me
        self.BinObject_be = BinObject_be
        self.FilterObject_fi = fi.Filters(self.LensName_str, self.Metric_me,
                                          self.DebugMode_bol)
        self.PointCloud_npArray = None
        self.FilteredPointCloud_npArray = None
  
    def filter_point_cloud(self,PointCloud_npArray):
        ''' filtered  applies filter from Filters.py, sorts on filter
        variable and places the points into bins.
        '''
        
        
        self.PointCloud_npArray = PointCloud_npArray

        if self.DebugMode_bol == True:
            print("In Lens.filtered: The PointCloud_npArray itself:")
            print(self.PointCloud_npArray)

        #FilteredPointCloud_npArray is sorted after filter size.
        self.FilteredPointCloud_npArray = self.filterpoint()

        if self.DebugMode_bol == True:
            print("In Lens.filtered: PointCloud_npArray after filter + sorting")
            print(self.FilteredPointCloud_npArray)

        #bins and adds a column of binning data
        self.FilteredPointCloud_npArray = self.BinObject_be.applybins(self.FilteredPointCloud_npArray)
        
        return self.FilteredPointCloud_npArray

    def filterpoint(self):
        ''' The function filterpoint applies the filter specified as
        self.lens to each point in the PointCloud_npArray.
        '''
        
        
        #creates filter for each point
        self.FilteredPointCloud_npArray = self.FilterObject_fi.applyfilter(self.PointCloud_npArray)
        if self.DebugMode_bol == True:
            print("In Lens.filterpoint: Cloud after added filthers:")
            print(self.FilteredPointCloud_npArray)
        
        #sorts the filtered PointCloud_npArrays on filter variable
        temporaryfiltered = np.zeros((self.FilteredPointCloud_npArray.shape[0],self.FilteredPointCloud_npArray.shape[1]))
        countvar = 0
        for index in np.lexsort((self.FilteredPointCloud_npArray[:,0],self.FilteredPointCloud_npArray[:,1])):
            temporaryfiltered[countvar] = self.FilteredPointCloud_npArray[index,:]
            countvar = countvar+1
        self.FilteredPointCloud_npArray = temporaryfiltered
        
        return self.FilteredPointCloud_npArray
