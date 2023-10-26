

"""General utilities.
"""

import time
import numpy as np
from matplotlib import pyplot as plt
from scipy.interpolate import InterpolatedUnivariateSpline
from scipy.optimize import curve_fit








class ProbDensityF(InterpolatedUnivariateSpline):
    """This class defines a probability density function, it is characterized by a cumulative density function cdf, and a ppf.
    It has the prob methods which returns the probability to find a number between x1 and x2.
    Rnd method generate a variable size ndarray of RNG numbers.
    meanvalue method return the mean value betwen 0 and 1. 
    """
    def __init__(self,x,y):
        InterpolatedUnivariateSpline.__init__(self,x,y) 
        """the pdf class is inheriting from the scipy class InterpolatedUnivariateSpline
        """
        ycdf = np.array([self.integral(x[0],xcdf) for xcdf in x])
        self.cdf = InterpolatedUnivariateSpline(x, ycdf)
        xppf, ippf = np.unique(ycdf, return_index=True)
        yppf = x[ippf]
        self.ppf = InterpolatedUnivariateSpline(xppf, yppf)
    
    def prob(self, x1, x2):
        """Calculates probability to find a number between x1 and x2, input are floats.
	"""
        return self.cdf(x2) - self.cdf(x1)

    def rnd(self, size = 1000):
        """ Returns a ndarray of size 1000 of random number distributed according to the pdf
            function
        """
        return self.ppf(np.random.uniform(size = size))

    def meanvalue(x,y):
    	"""Returns meanvalue between 0 and 1
    	"""
    	return InterpolatedUnivariateSpline(x,y*x).integral(0,1)
    def value(self, x):
        """ Returns value of pdf calculated on a generic ndarray, it is based on inheritance from the scipy InterpolatedUnivariateSpline class
        """
        return self.__call__(x)
	
    def error(self,x,y):
        """Returns the numerical error being made by using spline approximation
        """
    	return np.mean(y - self.__call__(x))
	
	

