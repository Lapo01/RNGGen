import time
import numpy as np
from matplotlib import pyplot as plt
from scipy.interpolate import InterpolatedUnivariateSpline
from scipy.optimize import curve_fit






#Ok, let's first define a pdf class: a pdf is characterized by its ppf, cf



class ProbDensityF(InterpolatedUnivariateSpline):
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
        """
	    """
        return self.cdf(x2) - self.cdf(x1)

    def rnd(self, size = 1000):
        """ Returns a ndarray of size 1000 of random number distributed according to the pdf
            function
        """
        return self.ppf(np.random.uniform(size = size))
	
	
	
	
	
	

