'''A class that handles the metric for the mapper algorithm.
'''


import numpy as np

from scipy.spatial import distance

class Metric:
    def __init__(self, MetricName_str, DebugMode_bol = False):
        '''Initiates with MetricName_str.
        '''
        
        self.MetricName_str = MetricName_str


    def get_metric(self):
        '''Returns the name of the metric.
        '''
        
        
        return self.MetricName_str
