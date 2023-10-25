.. RNGGen documentation master file, created by
   sphinx-quickstart on Mon Oct 23 16:09:01 2023.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

RNGGen
==================================
''RNGGen'' is a package that enables ones to take a certain particle density function and generate random numbers.

.. code-block:: python

   from RNGGen.Code import ProbDensityF

   x = np.linspace(0.,1.,101)

   y = 2.*x

   pdf = ProbDensityF(x,y)

   rnd = pdf.rnd(100000)

   plt.hist(rnd, bins = 200)

   plt.show()

   
   
.. toctree::
   :maxdepth: 2
   :caption: Contents:

   install 
   api

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
